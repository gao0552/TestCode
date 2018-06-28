# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 22:24:42 2018

@author: Administrator
"""

import pandas as pd
pd.set_option('display.width',450)

import plotly as py
import plotly.graph_objs as pygo
pyplt=py.offline.plot

#read the data
df=pd.read_csv(r'F:\Python Files\Python Project\Github\PythonPlotlyCodes\PythonPlotlyCodes\Chapter02\dat\tk01_m15.csv')
df9=df[:10]
print(df9)

idx=df9['xtim']
xd0=(df9['close']-27)*50
df2=df9.copy(deep=True)
df2['xd1']=xd0-10
df2['xd2']=xd0
df2['xd3']=xd0+10
print('xd2\n',df2)

xtr1=pygo.Scatter(
        x=idx,
        y=df2['xd1'],
        mode='markers',
        name='xtrl-markers'
        )
xtr2=pygo.Scatter(
        x=idx,
        y=df2['xd2'],
        mode='lines+markers',
        name='xtrl-lines+markers',
        marker=dict(
                size=5,
                color='rgb(155,155,155)',
                line=dict(
                        width=4,
                        color='rgb(0,0,0)'
                        )
                )
        )
xtr3=pygo.Scatter(
        x=idx,
        y=df2['xd3'],
        mode='lines',
        name='xtrl-lines'        
        )

xdat=pygo.Data([xtr1,xtr2,xtr3])
layout=pygo.Layout(
        title='收盘价-15分钟分时数据',
        xaxis=pygo.XAxis(tickangle=-15)
        )
fig=pygo.Figure(data=xdat,layout=layout)
pyplt(fig,filename='./result/scatter_apply.html')




