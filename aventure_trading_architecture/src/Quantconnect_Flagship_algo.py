{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red88\green138\blue67;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c41525\c59950\c33208;\cssrgb\c100000\c100000\c100000\c0;}
\margl1440\margr1440\vieww17180\viewh12840\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
#region imports\
from AlgorithmImports import *\
#undergone\
\
"""\
Aventure Trading Framework (Educational Prototype)\
\
This file represents an early-stage version of our research framework used to explore\
how asset universes, indicators, and portfolio construction interact\
in Quantconnect and make event-driven trades. Note: this was built on Quantconnects IDE.\
\
Important Note:\
- This is NOT our production grade strategy\
- Proprietary logic, optimization, and execution safeguards are omitted\
- The focus is on structure, readability, and learnings\
"""\
\
class ResearchTrendFramework(QCAlgorithm):\
\
    def Initialize(self):\
        """\
        Initialize the research environment:\
        - Define backtest window\
        - Set capital\
        - Configure universe and indicators\
        """\
\
        self.SetStartDate(2003, 1, 1)\
        self.SetCash(10000)\
\
        # Asset universe (chosen to represent broad asset classes)\
        self.symbols = [\'93Asset1\'94, \'93Asset2\'94, \'93Asset3\'94, \'93Asset4\'94, \'93Asset\'945]\
\
        # Store indicators by symbol\
        self.indicators = \{\}\
\
        # Approximate x-month moving average (~210 trading days)\
        self.lookback_period = our_chosen_lookback period was put here\
        self.SetWarmUp(self.lookback_period)\
\
        for ticker in self.symbols:\
            equity = self.AddEquity(ticker, Resolution.Daily)\
            self.indicators[ticker] = self.SMA(\
                equity.Symbol,\
                self.lookback_period,\
                Resolution.Daily\
            )\
\
        # Schedule a periodic rebalance\
        self.Schedule.On(\
            self.DateRules.WeekStart(self.symbols[0]),\
            self.TimeRules.AfterMarketOpen(self.symbols[0]),\
            self.Rebalance\
        )\
\
    def determine_eligible_assets(self):\
        """\
        Determine which assets meet a simple trend criterion.\
\
        This method is intentionally made more straightforward and designed\
        for clarity rather than how we optimized it.\
        """\
        eligible = []\
\
        for symbol, sma in self.indicators.items():\
            if not sma.IsReady:\
                continue\
\
            price = self.Securities[symbol].Price\
            if price > sma.Current.Value:\
                eligible.append(symbol)\
\
        return eligible\
\
    def Rebalance(self):\
        """\
        Portfolio rebalance logic:\
        - Hold assets that meet the trend condition\
        - Exit positions that no longer qualify\
        """\
\
        eligible_assets = self.determine_eligible_assets()\
\
        # Identify currently invested positions\
        invested = [\
            x.Key.Value for x in self.Portfolio if x.Value.Invested\
        ]\
\
        # Exit assets that no longer qualify\
        for symbol in invested:\
            if symbol not in eligible_assets:\
                self.Liquidate(symbol)\
\
        # Simply allocate equally across eligible assets (this was modified later on)\
        if eligible_assets:\
            weight = 1.0 / len(eligible_assets)\
            for symbol in eligible_assets:\
                self.SetHoldings(symbol, weight)\
}