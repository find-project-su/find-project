# OKX Info Bot    | 2024-02-22 | ver. 0.1.0
import telebot
from telebot import types
import time
from datetime import datetime
import logging
import os
import colorama
from colorama import Fore, Style
from fINd_Text_OKX import fINd_msgText, fINd_btnText
from fINd_OKXRq import pubOKXRq, privateOKXRq


# Read tg_token from env
def ReadConf():
    fConf = {}
    try:
        # Read Bot configuration file
        ConfFile = str(os.path.dirname(os.path.abspath(__file__))) + '/fINd_conf_OKX.env'
        with open(ConfFile) as file:
            for line in file:
                if (line[0] != '#') & (line[0] != '\n'):
                    # Remove unused symbols
                    line = line.replace(' ', '')
                    key, *value = line.split('=')
                    fConf[key] = str(value[0]).replace('\n', '').replace('\'', '')
    except Exception as ExText:
        FormExText = Fore.RED + "The following ERROR is occurred: " + Style.RESET_ALL + str(ExText)
        FormExText += Fore.YELLOW + "\nOKX Info Bot has been terminated" + Style.RESET_ALL
        print(FormExText)
        exit()
    try:
        ConfMsg = Fore.GREEN + "-------------------------------------------\n"
        ConfMsg += "# Your Telegram settings: " + "\n"
        ConfMsg += "# TOKEN: " + fConf['token'] + "\n"
        if 'chatId' in fConf.keys():
            ConfMsg += "# Chat Id: " + fConf['chatId'] + "\n"
        ConfMsg += "# UserName: " + fConf['userName'] + "\n"
        ConfMsg += "-------------------------------------------\n"
        ConfMsg += "# Your OKX API settings: " + "\n"
        ConfMsg += "# api_key: " + fConf['api_key'] + "\n"
        ConfMsg += "# api_secret: " + fConf['api_secret'] + "\n"
        ConfMsg += "# api_passphrase: " + fConf['api_passphrase'] + "\n"
        ConfMsg += "-------------------------------------------\n"
        ConfMsg += "fINd Info Bot for OKX trading platfrom is running\n"
        ConfMsg += f"Start time: {datetime.now().strftime('%H:%M:%S - %Y-%m-%d')}\n"
        ConfMsg += "# Selected Language: " + fConf['language'] + "\n"
        ConfMsg += "-------------------------------------------\n" + Style.RESET_ALL
        print(ConfMsg)
    except Exception as ExText:
        FormExText = Fore.RED + "The following ERROR is occurred: Check value of " + Style.RESET_ALL + str(ExText)
        FormExText += Fore.YELLOW + "\nOKX Info Bot has been terminated" + Style.RESET_ALL
        print(FormExText)
        exit()
    return fConf


# Distribution function of risk level range by the comporision of the balance and position volume
def BalancePositionValue(accBalance: str,
                         accPositionsVolume: float):
    BalPosVal = float(accBalance) / abs(accPositionsVolume)
    if BalPosVal > 4:
        result = '01'
    elif BalPosVal > 2:
        result = '02'
    elif BalPosVal > 1:
        result = '03'
    elif BalPosVal > 0.6:
        result = '04'
    elif BalPosVal > 0.5:
        result = '05'
    elif BalPosVal > 0.4:
        result = '06'
    elif BalPosVal > 0.3:
        result = '07'
    elif BalPosVal > 0.2:
        result = '08'
    elif BalPosVal > 0.1:
        result = '09'
    else:
        result = '10'
    return result


colorama.init()
logFileStr = str(datetime.now().strftime('%Y-%m-%d')) + '_log_auto.log'
logging.basicConfig(level=logging.INFO,
                    filename=logFileStr,
                    format="[%(asctime)s] - [%(levelname)s] => %(message)s",
                    datefmt='%Y-%m-%d, %H:%M:%S')

# Global variables
# various ids
user_id = ''
# Start trading tag
isTradeRun = False
# Risk level by default is 1
riskList = [['01', '02', '03', '04', '05', '06', '07', '08', '09', '10'],
            ['\U0001F499 \U00000031\U0000FE0F\U000020E3',
             '\U0001F49A \U00000032\U0000FE0F\U000020E3',
             '\U0001F49A \U00000033\U0000FE0F\U000020E3',
             '\U0001F49B \U00000034\U0000FE0F\U000020E3',
             '\U0001F49B \U00000035\U0000FE0F\U000020E3',
             '\U0001F49B \U00000036\U0000FE0F\U000020E3',
             '\U0001F9E1 \U00000037\U0000FE0F\U000020E3',
             '\U0001F9E1 \U00000038\U0000FE0F\U000020E3',
             '\U0001F9E1 \U00000039\U0000FE0F\U000020E3',
             '\U00002764 \U0001F51F']]
riskLevel = ['01']
# Last message tag - list of 2 elements, 1: tag, 2: message-ID
lastMsgTag = ['Empty', 0]
warnMsgTag = ['Empty', 0]
# Position list with status ['Symbol', 'Amount', 'OpenPrice', 'ClosePrice', 'PnL']
# PnL = (ClosePrice - OpenPrice) * Amount * 0.001
tradeList = [['Empty', '0', '0', '0', '0']]

# Init the bot
# The token should be masked before puplish to repo
fINdConf = ReadConf()
# Create class objects
privOKXRq = privateOKXRq(str(fINdConf['api_key']),
                         str(fINdConf['api_secret']),
                         str(fINdConf['api_passphrase']),
                         False)
publicOKXRq = pubOKXRq()
fINd_buttonText = fINd_btnText(str(fINdConf['language']))
fINd_messageText = fINd_msgText(str(fINdConf['language']))

# Bot init
bot = telebot.TeleBot(str(fINdConf['token']), parse_mode='HTML')


# Bot start function
@bot.message_handler(commands=['start'])
def start(message):
    # Pause of 200ms between API Rq
    time.sleep(0.2)
    global user_id
    user_id = message.chat.id
    # Bot privacy settings ONLY for one user
    if message.chat.username != fINdConf['userName']:
        bot.send_message(user_id, text="This Bot is private. You can't use it")
    else:
        markup = types.InlineKeyboardMarkup()
        start_trade_btn = types.InlineKeyboardButton(fINd_buttonText.btnContinue(), callback_data='start_trade')
        markup.row(start_trade_btn)
        startMsgText = fINd_messageText.introMsgStr(message.chat.first_name)
        startMsg = bot.send_message(user_id,
                                    text=startMsgText,
                                    reply_markup=markup)
        # Pause of 300ms between API Rq
        time.sleep(0.3)
        # Send message about bot starting to the channel (Private)
        if lastMsgTag[0] == 'Empty' and 'chatId' in fINdConf.keys():
            MsgToChannelStr = fINd_messageText.toChannelMsgStr(message.chat.username)
            bot.send_message(str(fINdConf['chatId']), MsgToChannelStr)
        # Update last Message list
        lastMsgTag[0] = 'startMsg'
        lastMsgTag[1] = startMsg.message_id


# Bot back to main screen function
@bot.callback_query_handler(func=lambda callback: callback.data == "back_main")
def back_main_callback(callback):
    # Update buttons AND the message start_tradeMsg
    if lastMsgTag[0] == 'start_tradeMsg':
        # Pause of 300ms between API Rq
        time.sleep(0.3)
        markup = types.InlineKeyboardMarkup()
        start_trade_btn = types.InlineKeyboardButton(fINd_buttonText.btnContinue(), callback_data='start_trade')
        markup.row(start_trade_btn)
        bot.edit_message_text(fINd_messageText.helpMsgStr(),
                              chat_id=callback.message.chat.id,
                              message_id=lastMsgTag[1],
                              reply_markup=markup)
        # Update last Message list
        lastMsgTag[0] = 'back_mainMsg'


# Bot set risk level
@bot.callback_query_handler(func=lambda callback: callback.data == "start_trade")
def getAccountInfo(callback):
    # Set message markup
    markup = types.InlineKeyboardMarkup()
    get_acc_info = types.InlineKeyboardButton(fINd_buttonText.btnGetBalance(), callback_data='get_acc_info')
    back_main = types.InlineKeyboardButton(fINd_buttonText.btnBack(), callback_data='back_main')
    markup.row(get_acc_info)
    markup.row(back_main)
    if lastMsgTag[0] == 'startMsg':
        # Hide buttons
        bot.edit_message_reply_markup(chat_id=callback.message.chat.id,
                                      message_id=lastMsgTag[1])
        # Pause of 300ms between API Rq
        time.sleep(0.3)
        start_tradeMsg = bot.send_message(callback.message.chat.id, fINd_messageText.helpMsgStr(), reply_markup=markup)
        # Update last Message list
        lastMsgTag[0] = 'start_tradeMsg'
        lastMsgTag[1] = start_tradeMsg.message_id
    if lastMsgTag[0] == 'back_mainMsg':
        # Pause of 300ms between API Rq
        time.sleep(0.3)
        bot.edit_message_text(fINd_messageText.helpMsgStr(),
                              chat_id=callback.message.chat.id,
                              message_id=lastMsgTag[1],
                              reply_markup=markup)
        # Update last Message list
        lastMsgTag[0] = 'start_tradeMsg'
    if lastMsgTag[0] == 'mainTradeMsg':
        # Hide buttons
        bot.edit_message_reply_markup(chat_id=callback.message.chat.id,
                                      message_id=lastMsgTag[1])
        # Pause of 300ms between API Rq
        time.sleep(0.3)
        start_tradeMsg = bot.send_message(callback.message.chat.id, fINd_messageText.helpMsgStr(), reply_markup=markup)
        # Update last Message list
        lastMsgTag[0] = 'start_tradeMsg'
        lastMsgTag[1] = start_tradeMsg.message_id


# Bot is ready to trade function. Show Main Trading Msg
@bot.callback_query_handler(func=lambda callback: callback.data == 'get_acc_info')
def main_trade_screen(callback):
    # Pause of 200ms between API Rq
    time.sleep(0.2)
    # Request last price of BTCUSDPERP
    lastAvgPrice = publicOKXRq.getTicker("BTC-USDT", False)
    accountBalance = privOKXRq.getAccountBalance()
    accountPositions = privOKXRq.getFuturesPositions()
    accountOrders = privOKXRq.getFuturesOrders()
    # Hide buttons
    if lastMsgTag[0] == 'start_tradeMsg':
        bot.edit_message_text(fINd_messageText.helpMsgStr(),
                              chat_id=callback.message.chat.id,
                              message_id=lastMsgTag[1])
        # Pause of 200ms between API Rq
        time.sleep(0.2)
    # Set message markup
    markup = types.InlineKeyboardMarkup()
    back_start_trade = types.InlineKeyboardButton(fINd_buttonText.btnBack(), callback_data='start_trade')
    begin_trading = types.InlineKeyboardButton(fINd_buttonText.btnStart(),
                                               callback_data='begin_trading')
    markup.row(begin_trading)
    markup.row(back_start_trade)
    mainTradeMsg = bot.send_message(callback.message.chat.id,
                                    fINd_messageText.mainTradeMsgStr(riskList[1][riskList[0].index(riskLevel[0])],
                                                                     lastAvgPrice,
                                                                     accountBalance,
                                                                     accountPositions,
                                                                     accountOrders),
                                    reply_markup=markup)
    # Init risk level by default
    riskLevel[0] = '01'
    lastMsgTag[0] = 'mainTradeMsg'
    lastMsgTag[1] = mainTradeMsg.message_id


# Trading is begin !
@bot.callback_query_handler(func=lambda callback: callback.data == "begin_trading")
def begin_trading_callback(callback):
    # Start trading tag
    global isTradeRun
    isTradeRun = True
    # Set message markup
    markup = types.InlineKeyboardMarkup()
    back_main_trade_screen = types.InlineKeyboardButton(fINd_buttonText.btnStop(),
                                                        callback_data='stop_trading')
    markup.row(back_main_trade_screen)
    # Pause of 200ms between API Rq
    time.sleep(0.2)
    # Edit buttons
    bot.edit_message_reply_markup(chat_id=callback.message.chat.id,
                                  message_id=lastMsgTag[1],
                                  reply_markup=markup)

    # By While cycle request trading platform every 15 sec
    # Seconds counter
    j = 0
    while True:
        if isTradeRun:
            # Pause of 1s
            time.sleep(1)
            j += 1
            # If counter = 15, reset counter, send request to trading platform
            if j == 15:
                j = 0
                # Request last price of BTCUSDPERP
                lastAvgPrice = publicOKXRq.getTicker("BTC-USDT", False)
                accountBalance = privOKXRq.getAccountBalance()
                accountPositions = privOKXRq.getFuturesPositions()
                accountOrders = privOKXRq.getFuturesOrders()
                accountFills = privOKXRq.getFuturesFills()
                # Recalculate risk level according open position volume
                if len(accountPositions) > 0:
                    # The relation of deposit and open position volume
                    riskLevel[0] = BalancePositionValue(accountBalance[0],
                                                        accountPositions[0]["posCost"])
                # Bot message text
                mainMsg = fINd_messageText.mainTradeMsgStr(riskList[1][riskList[0].index(riskLevel[0])],
                                                           lastAvgPrice,
                                                           accountBalance,
                                                           accountPositions,
                                                           accountOrders)
                # Update message
                bot.edit_message_text(mainMsg,
                                      chat_id=callback.message.chat.id,
                                      message_id=lastMsgTag[1],
                                      reply_markup=markup)
                # Analyse open position list. Check send to channel conditions if the Channel is set previously.
                # Prepare the message when open and close positions
                # If there is no any open position and a position appears in accountPositions - send OPEN
                # OR previous position has been CLOSED and appears in accountPositions
                if 'chatId' in fINdConf.keys():
                    if ((len(tradeList) == 1 and len(accountPositions) > 0) or
                            (tradeList[len(tradeList) - 1][3] != '0' and len(accountPositions) > 0)):
                        PosSymbol = str(accountPositions[0]["symbol"])[:len(accountPositions[0]["symbol"]) - 4]
                        tradeList.append([PosSymbol,
                                          str(accountPositions[0]["currentQty"]),
                                          str(accountPositions[0]["avgEntryPrice"]), '0', '0'])
                        channelMsg = fINd_messageText.openPosMsgStr(riskList[1][riskList[0].index(riskLevel[0])],
                                                                    accountPositions
                                                                    )
                        bot.send_message(str(fINdConf['chatId']), channelMsg)
                    # If position has been open and then closed, tradeList Close Price == 0
                    if len(tradeList) > 1 and tradeList[len(tradeList) - 1][3] == '0' and len(accountPositions) == 0:
                        closePrice = float(accountFills[0]['price'])
                        PnL = ((closePrice - float(tradeList[len(tradeList) - 1][2])) *
                               int(tradeList[len(tradeList) - 1][1]) * 0.001)
                        # to tradeList insert Close Price and PnL
                        tradeList[len(tradeList) - 1][3] = str(closePrice)
                        tradeList[len(tradeList) - 1][4] = str(PnL)
                        channelMsg = fINd_messageText.closePosMsgStr(riskList[1][riskList[0].index(riskLevel[0])],
                                                                     tradeList[len(tradeList) - 1][0],
                                                                     int(tradeList[len(tradeList) - 1][1]),
                                                                     PnL,
                                                                     closePrice
                                                                     )
                        bot.send_message(str(fINdConf['chatId']), channelMsg)
                        riskLevel[0] = '01'
                    # If position has been open and then increased, tradeList Close Price == 0
                    if (len(tradeList) > 1 and
                            tradeList[len(tradeList) - 1][3] == '0' and
                            len(accountPositions) > 0 and
                            abs(int(tradeList[len(tradeList) - 1][1])) != abs(int(accountPositions[0]["currentQty"]))):
                        # Define the direction of position changing
                        if abs(int(tradeList[len(tradeList) - 1][1])) > abs(int(accountPositions[0]["currentQty"])):
                            changePosDirection = 'Decrease'
                        else:
                            changePosDirection = 'Increase'
                        # in tradeList update position open price and volume
                        tradeList[len(tradeList) - 1][1] = str(accountPositions[0]["currentQty"])
                        tradeList[len(tradeList) - 1][2] = str(accountPositions[0]["avgEntryPrice"])
                        channelMsg = fINd_messageText.changePosMsgStr(riskList[1][riskList[0].index(riskLevel[0])],
                                                                      accountPositions,
                                                                      changePosDirection
                                                                      )
                        bot.send_message(str(fINdConf['chatId']), channelMsg)


# Bot is ready to trade function. Show Main Trading Msg
@bot.callback_query_handler(func=lambda callback: callback.data == "stop_trading")
def stop_trading_callback(callback):
    global isTradeRun
    isTradeRun = False
    # Pause of 200ms between API Rq
    time.sleep(0.2)
    # Request last price of BTCUSDPERP
    lastAvgPrice = publicOKXRq.getTicker("BTC-USDT", False)
    accountBalance = privOKXRq.getAccountBalance()
    accountPositions = privOKXRq.getFuturesPositions()
    accountOrders = privOKXRq.getFuturesOrders()
    # Set message markup
    markup = types.InlineKeyboardMarkup()
    back_start_trade = types.InlineKeyboardButton(fINd_buttonText.btnBack(),
                                                  callback_data='start_trade')
    begin_trading = types.InlineKeyboardButton(fINd_buttonText.btnStart(),
                                               callback_data='begin_trading')
    markup.row(begin_trading)
    markup.row(back_start_trade)
    bot.edit_message_text(fINd_messageText.mainTradeMsgStr(riskList[1][riskList[0].index(riskLevel[0])],
                                                           lastAvgPrice,
                                                           accountBalance,
                                                           accountPositions,
                                                           accountOrders),
                          chat_id=callback.message.chat.id,
                          message_id=lastMsgTag[1],
                          reply_markup=markup)


# User message processing
@bot.message_handler(func=lambda message: True, content_types=telebot.util.content_type_media)
def handle_message(message):
    # Delete user message
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    # Delete previous bot warning message if it has been existed
    if warnMsgTag[0] == 'warnMsg':
        bot.delete_message(chat_id=message.chat.id, message_id=warnMsgTag[1])
    warnMsg = bot.send_message(message.chat.id, fINd_messageText.toUserMsgStr())
    warnMsgTag[0] = 'warnMsg'
    warnMsgTag[1] = warnMsg.message_id


bot.infinity_polling(none_stop=True)
