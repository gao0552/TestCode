# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 21:05:17 2018

@author: Administrator
"""

import plotly as py
import plotly.graph_objs as pygo
pyplt=py.offline.plot


#Create random data with numpy
import numpy as np
N=100
random_x=np.linspace(0,1,N)
random_y0=np.random.randn(N)+5
random_y1=np.random.randn(N)
random_y2=np.random.randn(N)-5

#Create traces
trace0=pygo.Scatter(
        x=random_x,
        y=random_y0,
        mode='markers',
        name='markers',
        marker=dict(
                size=10,
                color='rgba(152,0,0,0.8)',
                line=dict(
                        width=2,
                        color='rgba(0,0,0,0.5)',
                        
                        )
                )
                    )
trace1=pygo.Scatter(
        x=random_x,
        y=random_y1,
        mode='lines+markers',
        name='lines+markers',
        marker=dict(
                size=10,
                color='rgba(144,255,0,0.8)',
                line=dict(
                        width=2,
                        color='rgba(0,0,0,0.5)',
                        
                        )
                )        
                    )
trace2=pygo.Scatter(
        x=random_x,
        y=random_y2,
        mode='lines',
        name='lines',
        marker=dict(
                size=10,
                color='rgba(175,200,36,0.8)',
                line=dict(
                        width=2,
                        color='rgba(0,0,0,0.5)',
                        
                        )
                )
                    )

#Output the reslut
data=[trace0,trace1,trace2]
layout=dict(
        title='Styled Scatter',
        yaxis=dict(zeroline=True),
        xaxis=dict(zeroline=False)
        )
fig=dict(data=data,layout=layout)
pyplt(fig,link_text='to data',filename='./result/scatter_basic_demo.html')




