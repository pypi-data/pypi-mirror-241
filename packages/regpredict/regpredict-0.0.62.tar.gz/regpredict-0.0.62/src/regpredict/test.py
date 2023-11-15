import pandas as pd
from regbot import signal

df = pd.read_csv('../reinforce/regbot_v66_validation.csv')

y_pred = []
def getSignal(opening,high,ema_26,low,close,ratio4,close_grad,close_grad_neg):
    
    args = [opening,high,ema_26,low,close,ratio4,close_grad,close_grad_neg]
    try:
        return signal(*args)
    except Exception as e:
        print(e)

print(df.columns)
#print(df.columns)
df = df.sample(frac=1).reset_index(drop=True)
#print(df.head())
df = df[df['trade'] == 1].head(20)
#print(df.head())

df['result'] = df.apply(lambda row: getSignal(row['open'],row['high'],
                                              row['ema-26'],row['low'],row['close'],row['ratio4'],
                                              row['close-gradient'],row['close-gradient-neg']), axis=1)

print(df.head())

print(len(df[df['result'] == df['trade']]), len(df))
