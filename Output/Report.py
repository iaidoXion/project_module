import json
from datetime import datetime

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
libUrl = SETTING['REPORT']['HOST']
dailyStorageLocation = SETTING['REPORT']['DAILY']['StorageLocation']
weeklyStorageLocation = SETTING['REPORT']['WEEKLY']['StorageLocation']
dailyFileName = SETTING['REPORT']['DAILY']['FILENAME']
weeklyFileName = SETTING['REPORT']['WEEKLY']['FILENAME']
fileFormat = SETTING['REPORT']['FILEFORMAT']
fileNameDate = datetime.today().strftime("%Y%m%d")
reportCreateDate = datetime.today().strftime("%Y-%m-%d")


def plug_in(type):
    html_text = """
        <!DOCTYPE html>
        <html lang="ko">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>X-Factor """ + type + """ report</title>
                <link rel="shortcunt icon" href='""" + libUrl + """/static/img/X-Factor_favicon/favicon.ico'>
                <link rel="stylesheet" href='""" + libUrl + """/static/assets/css/vendor.min.css'>
                <link rel="stylesheet" href='""" + libUrl + """/static/assets/css/app.min.css'>
                <link rel="stylesheet" type="text/css" href='""" + libUrl + """/static/css/reportPageStyle/font/reportPage_font.css'>
                <link rel="stylesheet" type="text/css" href='""" + libUrl + """/static/css/reportPageStyle/reportPage_""" + type + """.css'>
            </head>
            <body class="theme-orange">
                <div id="app" class="app pt-0">
    """
    if type == 'daily':
        fileName = dailyFileName
        storageLocation = dailyStorageLocation
        html_text += """
                    <div class="daily-report-wrap">
                        <!-- BEGIN daily-report 1 page -->
                        <div class="daily-report">
                            <div class="daily-sub-page">
                                <!-- brand logo -->
                                <div class="sub-content brand">
                                    <div class="brand-logo">
                                        <img src='""" + libUrl + """/static/css/reportPageStyle/images/XFactor_logo.png' alt="x-factor로고">
                                    </div>
                                    <p class="brand-title">자산 리포트</p>
                                </div>
                                <!-- daily-report-content -->
                                <div class="sub-content daily-report-content">
                                    <div class="daily-report-content-right">
                                        <div class="daily-report-logo">
                                            <img src='""" + libUrl + """/static/css/reportPageStyle/images/Tanium_logo.png' alt="Tanium로고">
                                        </div>
                                        <p class="daily-report-text">
                                            일간 자산 리포트
                                        </p>
                                    </div>
                                    <div class="daily-report-content-left">
                                        <ul>
                                            <li>
                                                <p>리포트 생성일</p>
                                                <p>""" + reportCreateDate + """</p>
                                            </li>
                                            <li>
                                                <p>데이터 기간</p>
                                                <p>2022-09-26</p>
                                                <p>00:00:00</p>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                                <!-- BEGIN daily-asset-state -->
                                <div class="sub-content daily-asset-state">
                                    <div class="daily-asset-state-title">
                                        <p>사내 자산 현황</p>
                                    </div>
                                    <div class="daily-asset-state-content">
                                        <div class="daily-asset-state-item">
                                            <div class="card h-100 ">
                                                <div class="card-body daily-asset-state-frame">
                                                    <p class="daily-asset-state-text">총 자산 수</p>
                                                    <p class="daily-asset-state-count">54</p>
                                                </div>
                                                <div class="card-arrow">
                                                    <div class="card-arrow-top-left"></div>
                                                    <div class="card-arrow-top-right"></div>
                                                    <div class="card-arrow-bottom-left"></div>
                                                    <div class="card-arrow-bottom-right"></div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="daily-asset-state-item">
                                            <div class="card h-100">
                                                <div class="card-body daily-asset-state-frame">
                                                    <p class="daily-asset-state-text">전일 대비 증감</p>
                                                    <p class="daily-asset-state-count">35</p>
                                                </div>
                                                <div class="card-arrow">
                                                    <div class="card-arrow-top-left"></div>
                                                    <div class="card-arrow-top-right"></div>
                                                    <div class="card-arrow-bottom-left"></div>
                                                    <div class="card-arrow-bottom-right"></div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="daily-asset-state-item">
                                            <div class="card h-100">
                                                <div class="card-body daily-asset-state-frame">
                                                    <p class="daily-asset-state-text">신규 조치대상 자산 수</p>
                                                    <p class="daily-asset-state-count">54</p>
                                                </div>
                                                <div class="card-arrow">
                                                    <div class="card-arrow-top-left"></div>
                                                    <div class="card-arrow-top-right"></div>
                                                    <div class="card-arrow-bottom-left"></div>
                                                    <div class="card-arrow-bottom-right"></div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="daily-asset-state-item">
                                            <div class="card h-100">
                                                <div class="card-body daily-asset-state-frame">
                                                    <p class="daily-asset-state-text">전일 대비 증감</p>
                                                    <p class="daily-asset-state-count">35</p>
                                                </div>
                                                <div class="card-arrow">
                                                    <div class="card-arrow-top-left"></div>
                                                    <div class="card-arrow-top-right"></div>
                                                    <div class="card-arrow-bottom-left"></div>
                                                    <div class="card-arrow-bottom-right"></div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- END daily-asset-state -->

                                <!-- BEGIN asset-action-list -->
                                <div class="sub-content asset-action-list">
                                    <div class="asset-action-title">
                                        <p>조치 대상 자산 현황</p>
                                    </div>
                                    <div class="asset-action-sub-title">
                                        <p>조치 대상 자산 리스트</p>
                                    </div>
                                    <div class="asset-action-content">
                                        <div class="card h-280px">
                                            <div class="card-body asset-action-item">
                                                <table class="asset-action-table fs-10px">
                                                    <colgroup>
                                                        <col class="w1">
                                                        <col class="w2">
                                                        <col class="w3">
                                                        <col class="w4">
                                                        <col class="w5">
                                                        <col class="w6">
                                                        <col class="w7">
                                                        <col class="w8">
                                                        <col class="w9">
                                                    </colgroup>
                                                    <thead>
                                                    <tr>
                                                        <th scope="col">Computer ID</th>
                                                        <th scope="col">Computer Name</th>
                                                        <th scope="col">CPU</th>
                                                        <th scope="col">RAM</th>
                                                        <th scope="col">Disk</th>
                                                        <th scope="col">Logon History</th>
                                                        <th scope="col">Listen Port</th>
                                                        <th scope="col">Established Port</th>
                                                        <th scope="col">Days</th>
                                                    </tr>
                                                    </thead>
                                                    <tbody>
                                                    <tr>
                                                        <td>1</td>
                                                        <td>Com1</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>90</td>
                                                    </tr>
                                                    <tr>
                                                        <td>2</td>
                                                        <td>Com2</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>88</td>
                                                    </tr>
                                                    <tr>
                                                        <td>3</td>
                                                        <td>Com3</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>81</td>
                                                    </tr>
                                                    <tr>
                                                        <td>4</td>
                                                        <td>Com4</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>80</td>
                                                    </tr>
                                                    <tr>
                                                        <td>5</td>
                                                        <td>Com5</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>78</td>
                                                    </tr>
                                                    <tr>
                                                        <td>6</td>
                                                        <td>Com6</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>77</td>
                                                    </tr>
                                                    <tr>
                                                        <td>7</td>
                                                        <td>Com7</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>72</td>
                                                    </tr>
                                                    <tr>
                                                        <td>8</td>
                                                        <td>Com8</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>70</td>
                                                    </tr>
                                                    <tr>
                                                        <td>9</td>
                                                        <td>Com9</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>70</td>
                                                    </tr>
                                                    <tr>
                                                        <td>10</td>
                                                        <td>Com10</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>False</td>
                                                        <td>63</td>
                                                    </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                            <div class="card-arrow">
                                                <div class="card-arrow-top-left"></div>
                                                <div class="card-arrow-top-right"></div>
                                                <div class="card-arrow-bottom-left"></div>
                                                <div class="card-arrow-bottom-right"></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- END asset-action-list -->

                                <!-- BEGIN asset-usage-list -->
                                <div class="sub-content asset-usage-list">
                                    <div class="resource-usage-frame">
                                        <div class="resource-usage-sub-title">
                                            <p>리소스 사용량 변동 없는 자산 리스트</p>
                                        </div>
                                        <div class="resource-usage-content">
                                            <div class="card h-245px">
                                                <div class="card-body resource-usage-item">
                                                    <table class="resource-usage-table fs-10px">
                                                        <colgroup>
                                                            <col class="w10">
                                                            <col class="w11">
                                                        </colgroup>
                                                        <thead>
                                                        <tr>
                                                            <th scope="col">Computer ID</th>
                                                            <th scope="col">Computer Name</th>
                                                            <th>CPU</th>
                                                            <th>RAM</th>
                                                            <th>Disk</th>
                                                        </tr>
                                                        </thead>
                                                        <tbody>
                                                        <tr>
                                                            <td>1</td>
                                                            <td>Com1</td>
                                                            <td>False</td>
                                                            <td>False</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>2</td>
                                                            <td>Com2</td>
                                                            <td>False</td>
                                                            <td>False</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>3</td>
                                                            <td>Com3</td>
                                                            <td>False</td>
                                                            <td>False</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>4</td>
                                                            <td>Com4</td>
                                                            <td>False</td>
                                                            <td>False</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>5</td>
                                                            <td>Com5</td>
                                                            <td>False</td>
                                                            <td>False</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>6</td>
                                                            <td>Com6</td>
                                                            <td>False</td>
                                                            <td>False</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>7</td>
                                                            <td>Com7</td>
                                                            <td>False</td>
                                                            <td>False</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>8</td>
                                                            <td>Com8</td>
                                                            <td>False</td>
                                                            <td>False</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>9</td>
                                                            <td>Com9</td>
                                                            <td>False</td>
                                                            <td>False</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>10</td>
                                                            <td>Com10</td>
                                                            <td>False</td>
                                                            <td>False</td>
                                                            <td>False</td>
                                                        </tr>
                                                        </tbody>
                                                    </table>
                                                </div>
                                                <div class="card-arrow">
                                                    <div class="card-arrow-top-left"></div>
                                                    <div class="card-arrow-top-right"></div>
                                                    <div class="card-arrow-bottom-left"></div>
                                                    <div class="card-arrow-bottom-right"></div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="login-usage-frame">
                                        <div class="login-usage-sub-title">
                                            <p>로그인 기록 없는 자산 리스트</p>
                                        </div>
                                        <div class="login-usage-content">
                                            <div class="card h-245px">
                                                <div class="card-body login-usage-item">
                                                    <table class="login-usage-table fs-10px">
                                                        <colgroup>
                                                            <col class="w10">
                                                            <col class="w11">
                                                        </colgroup>
                                                        <thead>
                                                        <tr>
                                                            <th scope="col">Computer ID</th>
                                                            <th scope="col">Computer Name</th>
                                                            <th>Logon History</th>
                                                        </tr>
                                                        </thead>
                                                        <tbody>
                                                        <tr>
                                                            <td>1</td>
                                                            <td>Com1</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>2</td>
                                                            <td>Com2</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>3</td>
                                                            <td>Com3</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>4</td>
                                                            <td>Com4</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>5</td>
                                                            <td>Com5</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>6</td>
                                                            <td>Com6</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>7</td>
                                                            <td>Com7</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>8</td>
                                                            <td>Com8</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>9</td>
                                                            <td>Com9</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>10</td>
                                                            <td>Com10</td>
                                                            <td>False</td>
                                                        </tr>
                                                        </tbody>
                                                    </table>
                                                </div>
                                                <div class="card-arrow">
                                                    <div class="card-arrow-top-left"></div>
                                                    <div class="card-arrow-top-right"></div>
                                                    <div class="card-arrow-bottom-left"></div>
                                                    <div class="card-arrow-bottom-right"></div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- END asset-usage-list -->
                            </div>
                        </div>
                        <!-- END daily-report 1 page -->

                        <!-- BEGIN daily-report 2 page -->
                        <div class="daily-report">
                            <div class="daily-sub-page">
                                <!-- BEGIN asset-port-list -->
                                <div class="sub-content asset-port-list">
                                    <div class="listenPort-usage-frame">
                                        <div class="listenPort-usage-sub-title">
                                            <p>Listen Port 수량 변화 없는 자산 리스트</p>
                                        </div>
                                        <div class="listenPort-usage-content">
                                            <div class="card h-245px">
                                                <div class="card-body listenPort-usage-item">
                                                    <table class="listenPort-usage-table fs-10px">
                                                        <colgroup>
                                                            <col class="w10">
                                                            <col class="w11">
                                                        </colgroup>
                                                        <thead>
                                                        <tr>
                                                            <th scope="col">Computer ID</th>
                                                            <th scope="col">Computer Name</th>
                                                            <th>Listen Port</th>
                                                        </tr>
                                                        </thead>
                                                        <tbody>
                                                        <tr>
                                                            <td>1</td>
                                                            <td>Com1</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>2</td>
                                                            <td>Com2</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>3</td>
                                                            <td>Com3</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>4</td>
                                                            <td>Com4</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>5</td>
                                                            <td>Com5</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>6</td>
                                                            <td>Com6</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>7</td>
                                                            <td>Com7</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>8</td>
                                                            <td>Com8</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>9</td>
                                                            <td>Com9</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>10</td>
                                                            <td>Com10</td>
                                                            <td>False</td>
                                                        </tr>
                                                        </tbody>
                                                    </table>
                                                </div>
                                                <div class="card-arrow">
                                                    <div class="card-arrow-top-left"></div>
                                                    <div class="card-arrow-top-right"></div>
                                                    <div class="card-arrow-bottom-left"></div>
                                                    <div class="card-arrow-bottom-right"></div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="establishedPort-usage-frame">
                                        <div class="establishedPort-usage-sub-title">
                                            <p>Established Port 수량 변화 없는 자산 리스트</p>
                                        </div>
                                        <div class="establishedPort-usage-content">
                                            <div class="card h-245px">
                                                <div class="card-body establishedPort-usage-item">
                                                    <table class="establishedPort-usage-table fs-10px">
                                                        <colgroup>
                                                            <col class="w10">
                                                            <col class="w11">
                                                        </colgroup>
                                                        <thead>
                                                        <tr>
                                                            <th scope="col">Computer ID</th>
                                                            <th scope="col">Computer Name</th>
                                                            <th>Established Port</th>
                                                        </tr>
                                                        </thead>
                                                        <tbody>
                                                        <tr>
                                                            <td>1</td>
                                                            <td>Com1</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>2</td>
                                                            <td>Com2</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>3</td>
                                                            <td>Com3</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>4</td>
                                                            <td>Com4</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>5</td>
                                                            <td>Com5</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>6</td>
                                                            <td>Com6</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>7</td>
                                                            <td>Com7</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>8</td>
                                                            <td>Com8</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>9</td>
                                                            <td>Com9</td>
                                                            <td>False</td>
                                                        </tr>
                                                        <tr>
                                                            <td>10</td>
                                                            <td>Com10</td>
                                                            <td>False</td>
                                                        </tr>
                                                        </tbody>
                                                    </table>
                                                </div>
                                                <div class="card-arrow">
                                                    <div class="card-arrow-top-left"></div>
                                                    <div class="card-arrow-top-right"></div>
                                                    <div class="card-arrow-bottom-left"></div>
                                                    <div class="card-arrow-bottom-right"></div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- END asset-port-list -->

                                <!-- BEGIN sw-asset-info -->
                                <div class="sub-content sw-asset-info">
                                    <div class="sw-asset-title">
                                        <p>SW 자산 정보</p>
                                    </div>
                                    <div class="sw-asset-info-frame">
                                        <div class="sw-asset-state-frame">
                                            <div class="sw-asset-state-sub-title">
                                                <p>SW 설치 현황 정보</p>
                                            </div>
                                            <div class="sw-asset-state-content">
                                                <div class="card h-245px">
                                                    <div class="card-body sw-asset-state-chart">
                                                        <div id="dailyChartRadialBarChart"></div>
                                                    </div>
                                                    <div class="card-arrow">
                                                        <div class="card-arrow-top-left"></div>
                                                        <div class="card-arrow-top-right"></div>
                                                        <div class="card-arrow-bottom-left"></div>
                                                        <div class="card-arrow-bottom-right"></div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="sw-asset-version-frame">
                                            <div class="sw-asset-version-sub-title">
                                                <p>SW별 버전 리스트</p>
                                            </div>
                                            <div class="sw-asset-version-content">
                                                <div class="card h-245px">
                                                    <div class="card-body sw-asset-version-item">
                                                        <table class="sw-asset-version-table fs-10px">
                                                            <thead>
                                                            <tr>
                                                                <th>SoftWare</th>
                                                                <th>Version</th>
                                                                <th>Count</th>
                                                            </tr>
                                                            </thead>
                                                            <tbody>
                                                            <tr>
                                                                <td>V3</td>
                                                                <td>3.12</td>
                                                                <td>42</td>
                                                            </tr>
                                                            <tr>
                                                                <td>V3</td>
                                                                <td>3.08</td>
                                                                <td>21</td>
                                                            </tr>
                                                            <tr>
                                                                <td>V3</td>
                                                                <td>2.14</td>
                                                                <td>44</td>
                                                            </tr>
                                                            <tr>
                                                                <td>Zabbix</td>
                                                                <td>1.15</td>
                                                                <td>145</td>
                                                            </tr>
                                                            <tr>
                                                                <td>Zabbix</td>
                                                                <td>1.14</td>
                                                                <td>14</td>
                                                            </tr>
                                                            <tr>
                                                                <td>Zabbix</td>
                                                                <td>1.11</td>
                                                                <td>32</td>
                                                            </tr>
                                                            <tr>
                                                                <td>Forescout</td>
                                                                <td>4.4</td>
                                                                <td>151</td>
                                                            </tr>
                                                            <tr>
                                                                <td>Forescout</td>
                                                                <td>4.2</td>
                                                                <td>3</td>
                                                            </tr>
                                                            <tr>
                                                                <td>McAfee</td>
                                                                <td>4.14</td>
                                                                <td>81</td>
                                                            </tr>
                                                            <tr>
                                                                <td>McAfee</td>
                                                                <td>4.12</td>
                                                                <td>50</td>
                                                            </tr>
                                                            </tbody>
                                                        </table>
                                                    </div>
                                                    <div class="card-arrow">
                                                        <div class="card-arrow-top-left"></div>
                                                        <div class="card-arrow-top-right"></div>
                                                        <div class="card-arrow-bottom-left"></div>
                                                        <div class="card-arrow-bottom-right"></div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- END sw-asset-info -->

                                <!-- BEGIN failure-Symptom-info -->
                                <div class="sub-content failure-Symptom-info">
                                    <div class="failure-Symptom-title">
                                        <p>장애징후 정보</p>
                                    </div>
                                    <div class="failure-Symptom-sub-title">
                                        <p>그룹별 장애징후 연관관계</p>
                                    </div>
                                    <div class="failure-Symptom-content">
                                        <div class="card h-280px">
                                            <div class="card-body failure-Symptom-chart h-280px">
                                                <div id="dailyChartRadarChart"></div>
                                            </div>
                                            <div class="card-arrow">
                                                <div class="card-arrow-top-left"></div>
                                                <div class="card-arrow-top-right"></div>
                                                <div class="card-arrow-bottom-left"></div>
                                                <div class="card-arrow-bottom-right"></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- END failure-Symptom-info -->

                            </div>
                        </div>
                        <!-- END daily-report 2 page -->
                    </div>
        """
    if type == 'weekly':
        fileName = weeklyFileName
        storageLocation = weeklyStorageLocation
        html_text += """
                    <div class="weekly-report-wrap">
                        <!-- BEGIN weekly-report 1 page -->
                        <div class="weekly-report">
                            <div class="weekly-sub-page">
                                <!-- brand logo -->
                                <div class="sub-content brand">
                                    <div class="brand-logo">
                                        <img src='""" + libUrl + """/static/css/reportPageStyle/images/XFactor_logo.png' alt="x-factor로고">
                                    </div>
                                    <p class="brand-title">자산 리포트</p>
                                </div>
                                <!-- weekly-report-content -->
                                <div class="sub-content weekly-report-content">
                                    <div class="weekly-report-content-right">
                                        <div class="weekly-report-logo">
                                            <img src='""" + libUrl + """/static/css/reportPageStyle/images/Tanium_logo.png' alt="Tanium로고">
                                        </div>
                                        <p class="weekly-report-text">
                                            주간 자산 리포트
                                        </p>
                                    </div>
                                    <div class="weekly-report-content-left">
                                        <ul>
                                            <li>
                                                <p>리포트 생성일</p>
                                                <p>""" + reportCreateDate + """</p>
                                            </li>
                                            <li>
                                                <p>데이터 기간</p>
                                                <p>2022-09-20 00:00:00 ~ 2022-09-26 00:00:00</p>
                                            </li>
                                        </ul>
                                    </div>
                                </div>

                                <!-- BEGIN weekly-asset-state -->
                                <div class="sub-content weekly-asset-state">
                                    <div class="weekly-asset-state-title">
                                        <p>자산 통계 정보</p>
                                    </div>
                                    <div class="weekly-asset-state-content">
                                        <div class="weekly-asset-state-item">
                                            <div class="card h-100">
                                                <div class="card-body weekly-asset-state-frame">
                                                    <p class="weekly-asset-state-text">총 자산 수
                                                    </p>
                                                    <p class="weekly-asset-state-count">54</p>
                                                </div>
                                                <div class="card-arrow">
                                                    <div class="card-arrow-top-left"></div>
                                                    <div class="card-arrow-top-right"></div>
                                                    <div class="card-arrow-bottom-left"></div>
                                                    <div class="card-arrow-bottom-right"></div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="weekly-asset-state-item">
                                            <div class="card h-100">
                                                <div class="card-body weekly-asset-state-frame">
                                                    <p class="weekly-asset-state-text">전주 대비 자산증감 수</p>
                                                    <p class="weekly-asset-state-count">35</p>
                                                </div>
                                                <div class="card-arrow">
                                                    <div class="card-arrow-top-left"></div>
                                                    <div class="card-arrow-top-right"></div>
                                                    <div class="card-arrow-bottom-left"></div>
                                                    <div class="card-arrow-bottom-right"></div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="weekly-asset-state-item">
                                            <div class="card h-100">
                                                <div class="card-body weekly-asset-state-frame">
                                                    <p class="weekly-asset-state-text">주간 조치대상 자산 수</p>
                                                    <p class="weekly-asset-state-count">54</p>
                                                </div>
                                                <div class="card-arrow">
                                                    <div class="card-arrow-top-left"></div>
                                                    <div class="card-arrow-top-right"></div>
                                                    <div class="card-arrow-bottom-left"></div>
                                                    <div class="card-arrow-bottom-right"></div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="weekly-asset-state-item">
                                            <div class="card h-100">
                                                <div class="card-body weekly-asset-state-frame">
                                                    <p class="weekly-asset-state-text">조치 완료된 자산 수</p>
                                                    <p class="weekly-asset-state-count">35</p>
                                                </div>
                                                <div class="card-arrow">
                                                    <div class="card-arrow-top-left"></div>
                                                    <div class="card-arrow-top-right"></div>
                                                    <div class="card-arrow-bottom-left"></div>
                                                    <div class="card-arrow-bottom-right"></div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- END weekly-asset-state -->

                                <!-- BEGIN asset-device-state -->
                                <div class="sub-content asset-device-state">
                                    <div class="asset-device-state-title">
                                        <p>주간 자산 정보</p>
                                    </div>
                                    <div class="asset-device-state-sub-title">
                                        <p>자산 증감 현황 (Top 3)</p>
                                        <p>2022/09/20 ~ 2022/09/26</p>
                                    </div>
                                    <div class="asset-device-state-content">
                                        <div class="card h-280px">
                                            <div class="card-body asset-device-state-item d-flex">
                                                <div class="col-3 d-flex asset-device-item-content">
                                                    <div class="col-9 small">
                                                        <p class="asset-device-item text-truncate">Virtual</p>
                                                        <p class="asset-device-item text-truncate">Desktop</p>
                                                        <p class="asset-device-item text-truncate">NoteBook</p>
                                                        <p class="asset-device-item text-truncate">Rack</p>
                                                        <p class="asset-device-item text-truncate">Etc</p>
                                                    </div>
                                                    <div class="col-3 small">
                                                        <p class="asset-device-count">10</p>
                                                        <p class="asset-device-count">21</p>
                                                        <p class="asset-device-count">10</p>
                                                        <p class="asset-device-count">21</p>
                                                        <p class="asset-device-count">5</p>
                                                    </div>
                                                </div>
                                                <div class="col-9">
                                                    <div id="weeklyChart_deviceAsset"></div>
                                                </div>
                                            </div>
                                            <div class="card-arrow">
                                                <div class="card-arrow-top-left"></div>
                                                <div class="card-arrow-top-right"></div>
                                                <div class="card-arrow-bottom-left"></div>
                                                <div class="card-arrow-bottom-right"></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- END asset-device-state -->

                                <!-- BEGIN asset-device-list -->
                                <div class="sub-content asset-device-list">
                                    <div class="asset-action-frame">
                                        <div class="asset-action-sub-title">
                                            <p>금주 발생 조치 대상 자산 리스트 (Top 3)</p>
                                        </div>
                                        <div class="asset-action-content">
                                            <div class="card h-245px">
                                                <div class="card-body asset-action-item">
                                                    <div id="weeklyChart_actionAsset"></div>
                                                </div>
                                                <div class="card-arrow">
                                                    <div class="card-arrow-top-left"></div>
                                                    <div class="card-arrow-top-right"></div>
                                                    <div class="card-arrow-bottom-left"></div>
                                                    <div class="card-arrow-bottom-right"></div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="asset-completed-frame">
                                        <div class="asset-completed-sub-title">
                                            <p>금주 조치 완료된 자산 리스트</p>
                                        </div>
                                        <div class="asset-completed-content">
                                            <div class="card h-245px">
                                                <div class="card-body asset-completed-item">
                                                    <div id="weeklyChart_completedAsset"></div>
                                                </div>
                                                <div class="card-arrow">
                                                    <div class="card-arrow-top-left"></div>
                                                    <div class="card-arrow-top-right"></div>
                                                    <div class="card-arrow-bottom-left"></div>
                                                    <div class="card-arrow-bottom-right"></div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- END asset-device-list -->
                            </div>
                        </div>
                        <!-- END weekly-report 1 page -->

                        <!-- BEGIN weekly-report 2 page -->
                        <div class="weekly-report">
                            <div class="weekly-sub-page">
                                <!-- BEGIN failure-symptom-state -->
                                <div class="sub-content failure-symptom-state">
                                    <div class="failure-symptom-state-title">
                                        <p>장애 징후</p>
                                    </div>
                                    <div class="failure-symptom-state-content">
                                        <div class="failure-symptom-case">
                                            <div class="failure-symptom-case-sub-title">
                                                <p>장애 징후 케이스별 주간 발생 현황</p>
                                            </div>
                                            <div class="failure-symptom-case-content">
                                                <div class="failure-symptom-case-item">
                                                    <div class="card h-100">
                                                        <div class="card-body failure-symptom-case-frame">
                                                            <p class="failure-symptom-case-text">CPU 사용량 > 80%
                                                            </p>
                                                            <p class="failure-symptom-case-count">54</p>
                                                        </div>
                                                        <div class="card-arrow">
                                                            <div class="card-arrow-top-left"></div>
                                                            <div class="card-arrow-top-right"></div>
                                                            <div class="card-arrow-bottom-left"></div>
                                                            <div class="card-arrow-bottom-right"></div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="failure-symptom-case-item">
                                                    <div class="card h-100">
                                                        <div class="card-body failure-symptom-case-frame">
                                                            <p class="failure-symptom-case-text">메모리 사용량 > 80%
                                                            </p>
                                                            <p class="failure-symptom-case-count">35</p>
                                                        </div>
                                                        <div class="card-arrow">
                                                            <div class="card-arrow-top-left"></div>
                                                            <div class="card-arrow-top-right"></div>
                                                            <div class="card-arrow-bottom-left"></div>
                                                            <div class="card-arrow-bottom-right"></div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="failure-symptom-case-item">
                                                    <div class="card h-100">
                                                        <div class="card-body failure-symptom-case-frame">
                                                            <p class="failure-symptom-case-text">Disk 사용량 > 90%
                                                            </p>
                                                            <p class="failure-symptom-case-count">36</p>
                                                        </div>
                                                        <div class="card-arrow">
                                                            <div class="card-arrow-top-left"></div>
                                                            <div class="card-arrow-top-right"></div>
                                                            <div class="card-arrow-bottom-left"></div>
                                                            <div class="card-arrow-bottom-right"></div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="failure-symptom-case-item">
                                                    <div class="card h-100">
                                                        <div class="card-body failure-symptom-case-frame">
                                                            <p class="failure-symptom-case-text">시스템 Crash 발생 건</p>
                                                            <p class="failure-symptom-case-count">23</p>
                                                        </div>
                                                        <div class="card-arrow">
                                                            <div class="card-arrow-top-left"></div>
                                                            <div class="card-arrow-top-right"></div>
                                                            <div class="card-arrow-bottom-left"></div>
                                                            <div class="card-arrow-bottom-right"></div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="failure-symptom-case-content mt-2">
                                                <div class="failure-symptom-case-item">
                                                    <div class="card h-100">
                                                        <div class="card-body failure-symptom-case-frame">
                                                            <p class="failure-symptom-case-text">필수 S/W1 패치 필요</p>
                                                            <p class="failure-symptom-case-count">54</p>
                                                        </div>
                                                        <div class="card-arrow">
                                                            <div class="card-arrow-top-left"></div>
                                                            <div class="card-arrow-top-right"></div>
                                                            <div class="card-arrow-bottom-left"></div>
                                                            <div class="card-arrow-bottom-right"></div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="failure-symptom-case-item">
                                                    <div class="card h-100">
                                                        <div class="card-body failure-symptom-case-frame">
                                                            <p class="failure-symptom-case-text">필수 S/W2 패치 필요</p>
                                                            <p class="failure-symptom-case-count">35</p>
                                                        </div>
                                                        <div class="card-arrow">
                                                            <div class="card-arrow-top-left"></div>
                                                            <div class="card-arrow-top-right"></div>
                                                            <div class="card-arrow-bottom-left"></div>
                                                            <div class="card-arrow-bottom-right"></div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="failure-symptom-case-item">
                                                    <div class="card h-100">
                                                        <div class="card-body failure-symptom-case-frame">
                                                            <p class="failure-symptom-case-text">필수 S/W3 패치 필요</p>
                                                            <p class="failure-symptom-case-count">36</p>
                                                        </div>
                                                        <div class="card-arrow">
                                                            <div class="card-arrow-top-left"></div>
                                                            <div class="card-arrow-top-right"></div>
                                                            <div class="card-arrow-bottom-left"></div>
                                                            <div class="card-arrow-bottom-right"></div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="failure-symptom-case-item">
                                                    <div class="card h-100">
                                                        <div class="card-body failure-symptom-case-frame">
                                                            <p class="failure-symptom-case-text">필수 S/W4 패치 필요</p>
                                                            <p class="failure-symptom-case-count">23</p>
                                                        </div>
                                                        <div class="card-arrow">
                                                            <div class="card-arrow-top-left"></div>
                                                            <div class="card-arrow-top-right"></div>
                                                            <div class="card-arrow-bottom-left"></div>
                                                            <div class="card-arrow-bottom-right"></div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="failure-symptom-chart">
                                            <div class="failure-symptom-chart-sub-title">
                                                <p>주차별 장애 징후별 증감 그래프</p>
                                            </div>
                                            <div class="failure-symptom-chart-content">
                                                <div class="card">
                                                    <div class="card-body failure-symptom-chart-item">
                                                        <div class="failure-Symptom-chart-frame">
                                                            <div class="failure-Symptom-chart-list-frame">
                                                                <div id="weeklyChart_usedCPU"></div>
                                                                <p class="weeklyChart_text">CPU 사용량 > 80%</p>
                                                            </div>
                                                            <div class="failure-Symptom-chart-list-frame">
                                                                <div id="weeklyChart_usedMemory"></div>
                                                                <p class="weeklyChart_text">Memory 사용량 > 80%</p>
                                                            </div>
                                                            <div class="failure-Symptom-chart-list-frame">
                                                                <div id="weeklyChart_usedDisk"></div>
                                                                <p class="weeklyChart_text">Disk 사용량 > 80%</p>
                                                            </div>
                                                        </div>
                                                        <div class="failure-Symptom-chart-frame mt-3">
                                                            <div class="failure-Symptom-chart-list-frame">
                                                                <div id="weeklyChart_usedSystem"></div>
                                                                <p class="weeklyChart_text">시스템 Crash 발생 건</p>
                                                            </div>
                                                            <div class="failure-Symptom-chart-list-frame">
                                                                <div id="weeklyChart_usedSw1"></div>
                                                                <p class="weeklyChart_text">필수 S/W1 패치 필요</p>
                                                            </div>
                                                            <div class="failure-Symptom-chart-list-frame">
                                                                <div id="weeklyChart_usedSw2"></div>
                                                                <p class="weeklyChart_text">필수 S/W2 패치 필요</p>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="card-arrow">
                                                        <div class="card-arrow-top-left"></div>
                                                        <div class="card-arrow-top-right"></div>
                                                        <div class="card-arrow-bottom-left"></div>
                                                        <div class="card-arrow-bottom-right"></div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- END failure-symptom-state -->
                        </div>
                    </div>
                    <!-- END weekly-report 2 page -->
    """
    html_text += """
                </div>
                <script src='""" + libUrl + """/static/js/jquery/jquery-3.6.0.min.js'></script>
                <script src='""" + libUrl + """/static/assets/plugins/bootstrap/dist/js/bootstrap.min.js'></script>
                <script src='""" + libUrl + """/static/assets/js/vendor.min.js'></script>
                <script src='""" + libUrl + """/static/assets/js/app.min.js'></script>
                <!-- apexchart -->
                <script src='""" + libUrl + """/static/assets/plugins/apexcharts/dist/apexcharts.min.js'></script>
                <script src='""" + libUrl + """/static/js/reportPageJS/reportPage_""" + type + """Chart.js'></script>
            </body>
        </html>
    """
    print(type)
    with open(storageLocation + fileName + fileNameDate + fileFormat, 'w', encoding="UTF-8") as html_file:
        html_file.write(html_text)
