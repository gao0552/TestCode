# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 20:46:00 2018

@author: Administrator
"""

import plotly as py
import plotly.graph_objs as pygo


trace0=pygo.Scatter(
        x=[1,2,3,4],
        y=[10,15,13,17]
        )

trace1=pygo.Scatter(
        x=[1,2,3,4],
        y=[16,5,11,9]
        )

data=pygo.Data([trace0,trace1])
py.offline.plot(data,filename=r'F:\Python Files\Python Project\Github\TestResult\first_start.html',show_link=True,link_text='基础数据')