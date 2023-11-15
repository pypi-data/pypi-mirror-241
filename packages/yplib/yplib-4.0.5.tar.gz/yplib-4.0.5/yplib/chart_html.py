import uuid


# 使用 echarts 的基本图表
def chart_html(option):
    uid = uuid.uuid4().hex
    s = ['<!DOCTYPE html>',
         '<html lang="zh-CN" style="height: 100%">',
         '<head>',
         '    <meta charset="utf-8">',
         '</head>',
         '<body style="height: 100%; margin: 0">',
         '<div id="container-uid-" style="height: 100%"></div>',
         '<script type="text/javascript" src="https://fastly.jsdelivr.net/npm/echarts/dist/echarts.min.js"></script>',
         '<script type="text/javascript">',
         '    var option-uid- = -option-;',
         '    var myChart-uid- = echarts.init(document.getElementById("container-uid-"), null, {',
         '        renderer: "canvas",',
         '        useDirtyRect: false,',
         '    });',
         '    myChart-uid-.setOption(option-uid-);',
         '    window.addEventListener("resize", myChart-uid-.resize);',
         '</script>',
         '</body>',
         '</html>',
         '']
    return list(map(lambda x: x.replace('-option-', '\n    '.join(option)).replace('-uid-', uid), s))


# 使用 table 的基本图表
def table_list_html(table_list, table_column):
    uid = uuid.uuid4().hex
    s = ['<!DOCTYPE html>',
         '<html>',
         '<head>',
         '    <meta charset="UTF-8">',
         '    <!-- import CSS -->',
         '    <link rel="stylesheet" href="https://unpkg.com/element-ui/lib/theme-chalk/index.css">',
         '</head>',
         '<body>',
         '<div id="app-uid-">',
         '    <el-table',
         '            :data="tableData-uid-"',
         '            border',
         '            stripe',
         '            max-height="800"',
         '            style="width: 100%">',
         '        -table_column-',
         '    </el-table>',
         '</div>',
         '</body>',
         '<!-- import Vue before Element -->',
         '<script src="https://unpkg.com/vue@2/dist/vue.js"></script>',
         '<!-- import JavaScript -->',
         '<script src="https://unpkg.com/element-ui/lib/index.js"></script>',
         '<script>',
         '    new Vue({',
         '        el: "#app-uid-",',
         '        data: function () {',
         '            return {',
         '                tableData-uid-: [',
         '                    -table_list-',
         '                ]',
         '            }',
         '        }',
         '    })',
         '</script>',
         '</html>']
    return list(map(lambda x: x.replace('-table_column-', '\n        '.join(table_column))
                    .replace('-table_list-', ',\n                    '.join(table_list))
                    .replace('-uid-', uid), s))


# table的 html 模板代码
# table_list = [{
#     date: '2016-05-02',
#     name: '王小虎',
#     address: '上海市普陀区金沙江路 1518 弄'
# }, {
#     date: '2016-05-04',
#     name: '王小虎',
#     address: '上海市普陀区金沙江路 1517 弄'
# }, {
#     date: '2016-05-03',
#     name: '王小虎',
#     address: '上海市普陀区金沙江路 1516 弄'
# }]
# title = {
#     date: '日期',
#     name: '名称',
#     address: '地址'
# }
def table_html(table, title=None):
    table_column = []
    table_list = []
    if title is None:
        title = {}
        for k in table[0]:
            title[k] = k
    for obj_one in table:
        l = []
        for k in obj_one:
            l.append(str(k) + ': "' + str(obj_one[k]) + '"')
        table_list.append('{' + ','.join(l) + '}')
    for k in title:
        # fixed
        pro = ''
        if len(table_column) == 0:
            pro += ' fixed'
        table_column.append('<el-table-column' + pro + ' sortable prop="' + str(k) + '" label="' + str(title[k]) + '"></el-table-column>')
    return table_list_html(table_list, table_column)


# 折线图的 html 模板代码
def line_stack_html():
    option = ['{',
              '    title: {',
              '        text: "-chart_name-",',
              '    },',
              '    tooltip: {',
              '        trigger: "axis",',
              '    },',
              '    dataZoom: [',
              '        {',
              '            show: true,',
              '            realtime: true,',
              '        },',
              '        {',
              '            type: "inside",',
              '            realtime: true,',
              '        },',
              '    ],',
              '    grid: {',
              '        left: "30px",',
              '        right: "30px",',
              '        bottom: "50px",',
              '        containLabel: true,',
              '    },',
              '    toolbox: {',
              '        feature: {',
              '            saveAsImage: {',
              '                pixelRatio: 5',
              '            },',
              '        },',
              '    },',
              '    yAxis: {',
              '        type: "value",',
              '    },',
              '    xAxis: {',
              '        type: "category",',
              '        boundaryGap: false,',
              '        data: -x_list-,',
              '    },',
              '    legend: {',
              '        -legend-,',
              '    },',
              '    series: -series-,',
              '}']
    return chart_html(option)


# 折线图的 html 模板代码
def line_area_html():
    option = ['{',
              '  tooltip: {',
              '    trigger: "axis",',
              '  },',
              '  title: {',
              '    text: "-chart_name-"',
              '  },',
              '  toolbox: {',
              '    feature: {',
              '       saveAsImage: {',
              '           pixelRatio: 5',
              '       },',
              '    }',
              '  },',
              '    grid: {',
              '        left: "30px",',
              '        right: "30px",',
              '        bottom: "50px",',
              '        containLabel: true,',
              '    },',
              '  xAxis: {',
              '    type: "category",',
              '    boundaryGap: false,',
              '    data: -x_list-',
              '  },',
              '  yAxis: {',
              '    type: "value",',
              '  },',
              '    dataZoom: [',
              '        {',
              '            show: true,',
              '            realtime: true,',
              '        },',
              '        {',
              '            type: "inside",',
              '            realtime: true,',
              '        },',
              '    ],',
              '  series: [',
              '    {',
              '      type: "line",',
              '      symbol: "none",',
              '      smooth: -smooth-,',
              '      sampling: "lttb",',
              '      itemStyle: {',
              '        color: "rgb(255, 70, 131)"',
              '      },',
              '      areaStyle: {',
              '        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [',
              '          {',
              '            offset: 0,',
              '            color: "rgb(255, 158, 68)"',
              '          },',
              '          {',
              '            offset: 1,',
              '            color: "rgb(255, 70, 131)"',
              '          }',
              '        ])',
              '      },',
              '      data: -y_list-',
              '    }',
              '  ]',
              '}']
    return chart_html(option)


# 饼图的 html 模板代码
def pie_html():
    option = ['{',
              '  title: {',
              '    text: "-chart_name-",',
              '    left: 10',
              '  },',
              '  tooltip: {',
              '    trigger: "item"',
              '  },',
              '    toolbox: {',
              '        feature: {',
              '            saveAsImage: {',
              '                pixelRatio: 5',
              '            },',
              '        },',
              '    },',
              '  legend: {',
              '    top: "5%",',
              '    left: "center"',
              '  },',
              '  series: [',
              '    {',
              '      name: "-chart_name-",',
              '      type: "pie",',
              '      radius: ["30%", "70%"],',
              '      itemStyle: {',
              '        borderRadius: 10,',
              '        borderColor: "#fff",',
              '        borderWidth: 1',
              '      },',
              '      emphasis: {',
              '        label: {',
              '          show: true,',
              '          fontSize: 30,',
              '          fontWeight: "bold"',
              '        }',
              '      },',
              '      labelLine: {',
              '        show: true',
              '      },',
              '      data: -x_list-',
              '    }',
              '  ]',
              '}']
    return chart_html(option)


# 柱状的 html 模板代码
def bar_html():
    option = ['{',
              '  title: {',
              '    text: "-chart_name-",',
              '    left: 10',
              '  },',
              '  toolbox: {',
              '    feature: {',
              '      dataZoom: {',
              '        yAxisIndex: false',
              '      },',
              '      saveAsImage: {',
              '            saveAsImage: {',
              '                pixelRatio: 5',
              '            },',
              '      }',
              '    }',
              '  },',
              '  tooltip: {',
              '    trigger: "axis",',
              '    axisPointer: {',
              '      type: "shadow"',
              '    }',
              '  },',
              '    grid: {',
              '        left: "30px",',
              '        right: "30px",',
              '        bottom: "50px",',
              '        containLabel: true,',
              '    },',
              '  dataZoom: [',
              '    {',
              '      type: "inside"',
              '    },',
              '    {',
              '      type: "slider"',
              '    }',
              '  ],',
              '  xAxis: {',
              '    data: -x_list-,',
              '    silent: false,',
              '    splitLine: {',
              '      show: false',
              '    },',
              '    splitArea: {',
              '      show: false',
              '    }',
              '  },',
              '  yAxis: {',
              '    splitArea: {',
              '      show: false',
              '    }',
              '  },',
              '  series: [',
              '    {',
              '      type: "bar",',
              '      data: -y_list-,',
              '      large: true',
              '    }',
              '  ]',
              '}']
    return chart_html(option)
