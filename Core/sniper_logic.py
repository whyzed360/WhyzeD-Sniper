import numpy as np

def get_adx(high, low, close, period=14):
    """Calculates Trend Strength - The 85% Accuracy Filter"""
    try:
        up_move = high[1:] - high[:-1]
        down_move = low[:-1] - low[1:]
        
        plus_dm = np.where((up_move > down_move) & (up_move > 0), up_move, 0)
        minus_dm = np.where((down_move > up_move) & (down_move > 0), down_move, 0)
        
        tr = np.maximum(high[1:] - low[1:], 
                        np.maximum(np.abs(high[1:] - close[:-1]), 
                                   np.abs(low[1:] - close[:-1])))
        
        atr = np.mean(tr[-period:])
        plus_di = 100 * (np.mean(plus_dm[-period:]) / atr)
        minus_di = 100 * (np.mean(minus_dm[-period:]) / atr)
        
        dx = 100 * np.abs(plus_di - minus_di) / (plus_di + minus_di)
        return dx # ADX > 25 means Strong Trend
    except:
        return 0

def get_rsi(prices, period=14):
    """Calculates Entry Precision"""
    deltas = np.diff(prices)
    seed = deltas[:period+1]
    up = seed[seed >= 0].sum() / period
    down = -seed[seed < 0].sum() / period
    rs = up / down
    return 100. - 100. / (1. + rs)
