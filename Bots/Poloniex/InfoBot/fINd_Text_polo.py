# Module with text of messages and buttons
from datetime import datetime


class fINd_msgText:
    # Bot message texts
    TradingPlatform = "Poloniex"
    Spaces = '\U00002003\U00002003'
    Dashes = '- - - - - - - - - - - - - - - - - - - - - - - - - - - -'

    def __init__(self, language):
        self.lang = language

    def toChannelMsgStr(self, userName: str):
        MsgStr = ''
        if self.lang == 'RU':
            MsgStr = f"&#129302 fINd-Info-bot запущен в: " \
                     f"{datetime.now().strftime('%H:%M:%S - %Y-%m-%d')}\n" \
                     f"Пользователем: <b>@{userName}</b>"
        if self.lang == 'EN':
            MsgStr = f"&#129302 fINd-Info-bot is started at: " \
                     f"{datetime.now().strftime('%H:%M:%S - %Y-%m-%d')}\n" \
                     f"by User: <b>@{userName}</b>"
        return MsgStr

    def introMsgStr(self, userFirstName: str):
        MsgStr = ''
        if self.lang == 'RU':
            MsgStr = f"Привет, <b>{userFirstName}</b>!\n\n&#129302 Я <b>fINd-Инфо-бот</b>. " \
                     f"В <b>автоматическом режиме</b> отслеживаю открытые позиции и заявки по " \
                     f"<b>Фьючерсам</b> на площадке <u>{self.TradingPlatform}</u>" \
                     f"и рассчитываю уровень риска позиций"
        if self.lang == 'EN':
            MsgStr = f"Hi, <b>{userFirstName}</b>!\n\n&#129302 I'm <b>fINd-Info-bot</b>. " \
                     f"<b>Automatically</b> monitor open positions and orders of " \
                     f"<b>Futures</b> at <u>{self.TradingPlatform}</u> trading platform " \
                     f"and calculate position's risk level"
        return MsgStr

    def helpMsgStr(self):
        MsgStr = ''
        if self.lang == 'RU':
            MsgStr = f'&#128073 Управление ботом только с помощью inline-кнопок под сообщениями' \
                     f'\n\n\u26a0\ufe0f Уровни риска рассчитаны для сценария:' \
                     f'\n{fINd_msgText.Spaces}\U0001F7E2 TakeProfit: [ <b>1.5%</b> ] OpenPrice' \
                     f'\n{fINd_msgText.Spaces}\U0001F534 StopLoss: [ <b>1.0%</b> ] OpenPrice' \
                     f'\n\n<b>Уровни риска</b> открытых позиций:' \
                     f'\n&#128153 &#49;&#65039;&#8419 - <b>Минимальный</b>. ' \
                     f'Возможный убыток не более 1%. Прибыль от 1.5%' \
                     f'\n&#128154 &#50;&#65039;&#8419, &#51;&#65039;&#8419 - Низкий. ' \
                     f'Возможный убыток 2-3%. Прибыль от 4%' \
                     f'\n&#128155 &#52;&#65039;&#8419, &#53;&#65039;&#8419, &#54;&#65039;&#8419 ' \
                     f'- Средний. Возможный убыток 4-6%. Прибыль от 6%' \
                     f'\n&#129505 &#55;&#65039;&#8419, &#56;&#65039;&#8419, &#57;&#65039;&#8419 ' \
                     f'- Высокий. Возможный убыток 8-10%. Прибыль от 10%' \
                     f'\n\U00002764 &#128287 - Максимальный. Возможный убыток <b>более</b> 10%. Прибыль от 12%'
        if self.lang == 'EN':
            MsgStr = f'&#128073 Bot control only by inline-buttons under messages' \
                     f'\n\n\u26a0\ufe0f Risk levels is calculated for the scenario:' \
                     f'\n{fINd_msgText.Spaces}\U0001F7E2 TakeProfit: [ <b>1.5%</b> ] OpenPrice' \
                     f'\n{fINd_msgText.Spaces}\U0001F534 StopLoss: [ <b>1.0%</b> ] OpenPrice' \
                     f'\n\n<b>Risk levels</b> of open positions:' \
                     f'\n&#128153 &#49;&#65039;&#8419 - <b>Minimum</b>. ' \
                     f'Possible loss is no more than 1%. Profit from 1.5%' \
                     f'\n&#128154 &#50;&#65039;&#8419, &#51;&#65039;&#8419 - Low. ' \
                     f'Possible loss 2-3%. Profit from 4%' \
                     f'\n&#128155 &#52;&#65039;&#8419, &#53;&#65039;&#8419, &#54;&#65039;&#8419 ' \
                     f'- Average. Possible loss 4-6%. Profit from 6%' \
                     f'\n&#129505 &#55;&#65039;&#8419, &#56;&#65039;&#8419, &#57;&#65039;&#8419 ' \
                     f'- High. Possible loss 8-10%. Profit from 10%' \
                     f'\n\U00002764 &#128287 - Maximum. Possible loss of <b>more than</b> 10%. Profit from 12%'
        return MsgStr

    def toUserMsgStr(self):
        MsgStr = ''
        if self.lang == 'RU':
            MsgStr = f"&#128274 Сообщения от пользователя не обрабатываются.\n" \
                     f'Для управления ботом используйте <i>inline</i>-кнопки под сообщениям от бота'
        if self.lang == 'EN':
            MsgStr = f"&#128274 Messages from the user are not processed.\n" \
                     f'To control the bot use <i>inline</i>-buttons under bot messages'
        return MsgStr

    def mainTradeMsgStr(self,
                        riskLevelSymbol: str,
                        lastPrice: str,
                        accBalance: list,
                        accPositions: list,
                        accOrders: list):
        OpenPosStr = ''
        if self.lang == 'RU':
            OpenPosStr = f"\n<b>Открытые позиции: </b>" \
                         f'\n{fINd_msgText.Spaces}Открыте позиции ОТСУТСТВУЮТ\n'
        if self.lang == 'EN':
            OpenPosStr = f"\n<b>Open positions: </b>" \
                         f'\n{fINd_msgText.Spaces}Open positions is ABSENT\n'
        OpenOrdStr = ''
        if self.lang == 'RU':
            OpenOrdStr = f"\n<b>Открытые заявки:</b>" \
                         f'\n{fINd_msgText.Spaces}Открыте заявки ОТСУТСТВУЮТ'
        if self.lang == 'EN':
            OpenOrdStr = f"\n<b>Open orders:</b>" \
                         f'\n{fINd_msgText.Spaces}Open orders is ABSENT'
        # Если есть открытые позиции форматируем строку
        if len(accPositions) > 0:
            if self.lang == 'RU':
                OpenPosStr = f"\n<b>Открытые позиции: [ {len(accPositions)} ]\n</b>"
            if self.lang == 'EN':
                OpenPosStr = f"\n<b>Open positions: [ {len(accPositions)} ]\n</b>"
            # Цикл по всем открытым позициям
            for j in range(len(accPositions)):
                if accPositions[j]['currentQty'] > 0:  # Buy LONG position
                    Direction = '\U0001F131\U0001F144\U0001F148'
                    TakeProfit = accPositions[j]["avgEntryPrice"] * 1.015
                    StopLoss = accPositions[j]["avgEntryPrice"] * 0.99
                else:  # Sell SHORT position
                    Direction = '\U0001F182\U0001F174\U0001F17B\U0001F17B'
                    TakeProfit = accPositions[j]["avgEntryPrice"] * 0.985
                    StopLoss = accPositions[j]["avgEntryPrice"] * 1.01
                # Индикатор прибыльности позиции. Зеленый - в плюсе. Красный - в минусе
                if accPositions[j]['unrealisedPnl'] > 0:
                    signPnL = '\U0001F7E2'
                else:
                    signPnL = '\U0001F534'
                PosSymbol = str(accPositions[j]["symbol"])[:len(accPositions[j]["symbol"]) - 4]
                OpenPosStr += f'{fINd_msgText.Spaces}<b>[</b> {j + 1} <b>]</b> {Direction}  {PosSymbol}' \
                              f'\n{fINd_msgText.Spaces}{fINd_msgText.Spaces}PnL: ' \
                              f'<b>{"{:.1f}".format(accPositions[j]["unrealisedPnl"])}</b> {signPnL}' \
                              f'\n{fINd_msgText.Spaces}{fINd_msgText.Spaces}TP / SL: ' \
                              f'<b>[</b> {"{:.0f}".format(TakeProfit)} <b>]</b>' \
                              f' / <b>[</b> {"{:.0f}".format(StopLoss)} <b>]</b>' \
                              f'\n{fINd_msgText.Spaces}{fINd_msgText.Spaces}Amount (lot): ' \
                              f'{accPositions[j]["currentQty"]}' \
                              f'\n{fINd_msgText.Spaces}{fINd_msgText.Spaces}Margin: ' \
                              f'{"{:.1f}".format(accPositions[j]["maintMargin"])}' \
                              f'\n{fINd_msgText.Spaces}{fINd_msgText.Spaces}Entry Price: ' \
                              f'<b>{"{:.1f}".format(accPositions[j]["avgEntryPrice"])}</b>\n'
        # Если есть открытые заявки форматируем строку
        if len(accOrders) > 0:
            if self.lang == 'RU':
                OpenOrdStr = f"\n<b>Открытые заявки: [ {len(accOrders)} ]\n</b>"
            if self.lang == 'EN':
                OpenOrdStr = f"\n<b>Open orders: [ {len(accOrders)} ]\n</b>"
            # Цикл по всем заявка в книге заявок
            for j in range(len(accOrders)):
                if accOrders[j]['side'] == 'buy':  # Buy LONG order
                    Direction = '\U0001F131\U0001F144\U0001F148'
                else:  # Sell SHORT order
                    Direction = '\U0001F182\U0001F174\U0001F17B\U0001F17B'
                OrdSymbol = str(accOrders[j]["symbol"])[:len(accOrders[j]["symbol"]) - 4]
                OpenOrdStr += f'{fINd_msgText.Spaces}<b>[</b> {j + 1} <b>]</b> {OrdSymbol}: {Direction}' \
                              f'\n{fINd_msgText.Spaces}{fINd_msgText.Spaces}Amount (lot): ' \
                              f'<b>{accOrders[j]["size"]}</b>' \
                              f'\n{fINd_msgText.Spaces}{fINd_msgText.Spaces}Price: <b>{accOrders[j]["price"]}</b>\n'
        # Формируем строку всего сообщения
        MsgStr = ''
        if self.lang == 'RU':
            MsgStr = f"\U0000231A Время: {datetime.now().strftime('%H:%M:%S - %Y-%m-%d')}\n" \
                     f"\nКурс BTC/USDT: <b>{lastPrice}</b>" \
                     f"\nБаланс USDT:" \
                     f"\n{fINd_msgText.Spaces}Полный: <b>{accBalance[0]}</b>" \
                     f"\n{fINd_msgText.Spaces}Доступный: <b>{accBalance[1]}</b>" \
                     f"\nУровень риска: {riskLevelSymbol}" \
                     f"\n{fINd_msgText.Dashes}" \
                     f"{OpenPosStr}" \
                     f"{fINd_msgText.Dashes}" \
                     f"{OpenOrdStr}"
        if self.lang == 'EN':
            MsgStr = f"\U0000231A Time: {datetime.now().strftime('%H:%M:%S - %Y-%m-%d')}\n" \
                     f"\nExRate BTC/USDT: <b>{lastPrice}</b>" \
                     f"\nBalance USDT:" \
                     f"\n{fINd_msgText.Spaces}Total: <b>{accBalance[0]}</b>" \
                     f"\n{fINd_msgText.Spaces}Available: <b>{accBalance[1]}</b>" \
                     f"\nRisk Level: {riskLevelSymbol}" \
                     f"\n{fINd_msgText.Dashes}" \
                     f"{OpenPosStr}" \
                     f"{fINd_msgText.Dashes}" \
                     f"{OpenOrdStr}"
        return MsgStr

    def openPosMsgStr(self,
                      riskLevelSymbol: str,
                      accPositions: list):
        OpenPosStr = ''
        if self.lang == 'RU':
            OpenPosStr = f"\n\U000025B6\U0000FE0F <b>ОТКРЫТА позиция: \n</b>"
        if self.lang == 'EN':
            OpenPosStr = f"\n\U000025B6\U0000FE0F <b>OPEN position: \n</b>"
        # Цикл по всем открытым позициям
        for j in range(len(accPositions)):
            if accPositions[j]['currentQty'] > 0:  # Buy LONG position
                Direction = '\U0001F131\U0001F144\U0001F148'
                TakeProfit = accPositions[j]["avgEntryPrice"] * 1.015
                # StopLoss = accPositions[j]["avgEntryPrice"] * 0.99
            else:  # Sell SHORT position
                Direction = '\U0001F182\U0001F174\U0001F17B\U0001F17B'
                TakeProfit = accPositions[j]["avgEntryPrice"] * 0.985
                # StopLoss = accPositions[j]["avgEntryPrice"] * 1.01
            PosSymbol = str(accPositions[j]["symbol"])[:len(accPositions[j]["symbol"]) - 4]
            OpenPosStr += f'{self.Spaces}<b>[</b> {j + 1} <b>]</b> {Direction}  {PosSymbol}:' \
                          f'\n{self.Spaces}{self.Spaces}' \
                          f'TakeProfit: <b>[</b> {"{:.1f}".format(TakeProfit)} <b>]</b>' \
                          f'\n{self.Spaces}{self.Spaces}' \
                          f'Amount (lot): {accPositions[j]["currentQty"]}' \
                          f'\n{self.Spaces}{self.Spaces}' \
                          f'Margin: {"{:.2f}".format(accPositions[j]["maintMargin"])}' \
                          f'\n{self.Spaces}{self.Spaces}' \
                          f'Entry Price: <b>{"{:.1f}".format(accPositions[j]["avgEntryPrice"])}</b>\n'
            # f' / <b>[</b> {"{:.1f}".format(StopLoss)} <b>]</b>' \
        # Формируем строку всего сообщения
        MsgStr = ''
        if self.lang == 'RU':
            MsgStr = f"\U0000231A Время: {datetime.now().strftime('%H:%M:%S - %Y-%m-%d')}\n" \
                     f"\nПлощадка: <b>{fINd_msgText.TradingPlatform}</b>" \
                     f"\nБазовая валюта: <b>{accPositions[0]['settleCurrency']}</b>" \
                     f"\nУровень риска: {riskLevelSymbol}" \
                     f"\n{self.Dashes}" \
                     f"{OpenPosStr}"
        if self.lang == 'EN':
            MsgStr = f"\U0000231A Time: {datetime.now().strftime('%H:%M:%S - %Y-%m-%d')}\n" \
                     f"\nPlatform: <b>{fINd_msgText.TradingPlatform}</b>" \
                     f"\nBase currency: <b>{accPositions[0]['settleCurrency']}</b>" \
                     f"\nRisk Level: {riskLevelSymbol}" \
                     f"\n{self.Dashes}" \
                     f"{OpenPosStr}"
        return MsgStr

    def closePosMsgStr(self,
                       riskLevelSymbol: str,
                       symbol: str,
                       amount: int,
                       PnL: float,
                       closePrice: float):
        OpenPosStr = ''
        if self.lang == 'RU':
            OpenPosStr = f"\n\u23f9\ufe0f <b>ЗАКРЫТА позиция: \n</b>"
        if self.lang == 'EN':
            OpenPosStr = f"\n\u23f9\ufe0f <b>CLOSE position: \n</b>"

        # Относительный PnL
        relPnL = (PnL * 100) / (abs(amount) * closePrice * 0.001)
        if amount > 0:  # Buy LONG position
            Direction = '\U0001F131\U0001F144\U0001F148'
        else:  # Sell SHORT position
            Direction = '\U0001F182\U0001F174\U0001F17B\U0001F17B'
        # Индикатор прибыльности позиции. Зеленый - в плюсе. Красный - в минусе
        if PnL > 0:
            signPnL = '\U0001F7E2'
        else:
            signPnL = '\U0001F534'
        if self.lang == 'RU':
            OpenPosStr += f'{self.Spaces}{Direction}  {symbol}: ' \
                          f'\n{self.Spaces}{self.Spaces}Close Price: <b>{"{:.1f}".format(closePrice)}</b>' \
                          f'\n{self.Spaces}{self.Spaces}Amount (lot): {amount}' \
                          f'\nРезультат сделки:\n{self.Spaces}' \
                          f'<b>{"{:.3f}".format(PnL)}</b> USDT ( {"{:.2f}".format(relPnL)}% ) {signPnL}'
        if self.lang == 'EN':
            OpenPosStr += f'{self.Spaces}{Direction}  {symbol}: ' \
                          f'\n{self.Spaces}{self.Spaces}Close Price: <b>{"{:.1f}".format(closePrice)}</b>' \
                          f'\n{self.Spaces}{self.Spaces}Amount (lot): {amount}' \
                          f'\nTrade Result:\n{self.Spaces}' \
                          f'<b>{"{:.3f}".format(PnL)}</b> USDT ( {"{:.2f}".format(relPnL)}% ) {signPnL}'
        # Формируем строку всего сообщения
        # Базовую валюту параметризовать
        MsgStr = ''
        if self.lang == 'RU':
            MsgStr = f"\U0000231A Время: {datetime.now().strftime('%H:%M:%S - %Y-%m-%d')}\n" \
                     f"\nПлощадка: <b>{fINd_msgText.TradingPlatform}</b>" \
                     f"\nБазовая валюта: <b>USDT</b>" \
                     f"\nУровень риска: {riskLevelSymbol}" \
                     f"\n{fINd_msgText.Dashes}" \
                     f"{OpenPosStr}"
        if self.lang == 'EN':
            MsgStr = f"\U0000231A Time: {datetime.now().strftime('%H:%M:%S - %Y-%m-%d')}\n" \
                     f"\nPlatform: <b>{fINd_msgText.TradingPlatform}</b>" \
                     f"\nBase currency: <b>USDT</b>" \
                     f"\nRisk Level: {riskLevelSymbol}" \
                     f"\n{fINd_msgText.Dashes}" \
                     f"{OpenPosStr}"
        return MsgStr

    def changePosMsgStr(self,
                        riskLevelSymbol: str,
                        accPositions: list,
                        changeDir: str):
        OpenPosStr = ''
        if changeDir == 'Increase':
            if self.lang == 'RU':
                OpenPosStr = f"\n\u2b06\ufe0f <b>УВЕЛИЧЕНА позиция: \n</b>"
            if self.lang == 'EN':
                OpenPosStr = f"\n\u2b06\ufe0f <b>INCREASE position: \n</b>"
        else:
            if self.lang == 'RU':
                OpenPosStr = f"\n\u2b07\ufe0f <b>УМЕНЬШЕНА позиция: \n</b>"
            if self.lang == 'EN':
                OpenPosStr = f"\n\u2b07\ufe0f <b>DECREASE position: \n</b>"
        # Цикл по всем открытым позициям
        for j in range(len(accPositions)):
            if accPositions[j]['currentQty'] > 0:  # Buy LONG position
                Direction = '\U0001F131\U0001F144\U0001F148'
                TakeProfit = accPositions[j]["avgEntryPrice"] * 1.015
                # StopLoss = accPositions[j]["avgEntryPrice"] * 0.99
            else:  # Sell SHORT position
                Direction = '\U0001F182\U0001F174\U0001F17B\U0001F17B'
                TakeProfit = accPositions[j]["avgEntryPrice"] * 0.985
                # StopLoss = accPositions[j]["avgEntryPrice"] * 1.01
            PosSymbol = str(accPositions[j]["symbol"])[:len(accPositions[j]["symbol"]) - 4]
            OpenPosStr += f'{self.Spaces}<b>[</b> {j + 1} <b>]</b> {Direction}  {PosSymbol}:' \
                          f'\n{self.Spaces}{self.Spaces}' \
                          f'TakeProfit: <b>[</b> {"{:.1f}".format(TakeProfit)} <b>]</b>' \
                          f'\n{self.Spaces}{self.Spaces}Amount (lot): {accPositions[j]["currentQty"]}' \
                          f'\n{self.Spaces}{self.Spaces}' \
                          f'Margin: {"{:.2f}".format(accPositions[j]["maintMargin"])}' \
                          f'\n{self.Spaces}{self.Spaces}' \
                          f'Entry Price: <b>{"{:.1f}".format(accPositions[j]["avgEntryPrice"])}</b>\n'
            # f' / <b>[</b> {"{:.1f}".format(StopLoss)} <b>]</b>' \
        # Формируем строку всего сообщения
        MsgStr = ''
        if self.lang == 'RU':
            MsgStr = f"\U0000231A Время: {datetime.now().strftime('%H:%M:%S - %Y-%m-%d')}\n" \
                     f"\nПлощадка: <b>{self.TradingPlatform}</b>" \
                     f"\nБазовая валюта: <b>{accPositions[0]['settleCurrency']}</b>" \
                     f"\nУровень риска: {riskLevelSymbol}" \
                     f"\n{self.Dashes}" \
                     f"{OpenPosStr}"
        if self.lang == 'EN':
            MsgStr = f"\U0000231A Time: {datetime.now().strftime('%H:%M:%S - %Y-%m-%d')}\n" \
                     f"\nPlatform: <b>{self.TradingPlatform}</b>" \
                     f"\nBase currency: <b>{accPositions[0]['settleCurrency']}</b>" \
                     f"\nRisk Level: {riskLevelSymbol}" \
                     f"\n{self.Dashes}" \
                     f"{OpenPosStr}"
        return MsgStr


class fINd_btnText:

    def __init__(self, language):
        self.lang = language

    # @classmethod
    def btnContinue(self):
        btnCaption = ''
        if self.lang == 'RU':
            btnCaption = f'\u27a1\ufe0f Продолжить'
        if self.lang == 'EN':
            btnCaption = f'\u27a1\ufe0f Continue'
        return btnCaption

    def btnGetBalance(self):
        btnCaption = ''
        if self.lang == 'RU':
            btnCaption = f'\U0001f4b0 Запрос баланса'
        if self.lang == 'EN':
            btnCaption = f'\U0001f4b0 Get Balance'
        return btnCaption

    def btnBack(self):
        btnCaption = ''
        if self.lang == 'RU':
            btnCaption = f'\U0001F519 Вернуться \U0001F519'
        if self.lang == 'EN':
            btnCaption = f'\U0001F519 Back to previous \U0001F519'
        return btnCaption

    def btnStart(self):
        btnCaption = ''
        if self.lang == 'RU':
            btnCaption = f'\U0001F680 Начать мониторинг \U000025B6\U0000FE0F'
        if self.lang == 'EN':
            btnCaption = f'\U0001F680 Start monitoring \U000025B6\U0000FE0F'
        return btnCaption

    def btnStop(self):
        btnCaption = ''
        if self.lang == 'RU':
            btnCaption = f'Остановить мониторинг \u23f9\ufe0f'
        if self.lang == 'EN':
            btnCaption = f'Stop monitoring \u23f9\ufe0f'
        return btnCaption
