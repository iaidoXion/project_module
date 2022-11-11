import json

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
libUrl = SETTING['Report']['URL']
libPort = SETTING['Report']['PORT']
def plug_in():
    html_text = """
        <!DOCTYPE html>
            <html lang="ko">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>X-Factor Daily Report</title>
                <link rel="shortcunt icon" href='http://"""+libUrl+""":"""+libPort+"""/static/img/X-Factor_favicon/favicon.ico'>
                <link rel="stylesheet" href='http://"""+libUrl+""":"""+libPort+"""/static/assets/css/vendor.min.css'>
                <link rel="stylesheet" href='http://"""+libUrl+""":"""+libPort+"""/static/assets/css/app.min.css'>
                <link rel="stylesheet" type="text/css" href='/Users/aidoi/X-Factor/static/css/reportPageStyle/font/reportPage_font.css'>
                <link rel="stylesheet" type="text/css" href='/Users/aidoi/X-Factor/static/css/reportPageStyle/reportPage_daily.css'>
            </head>
            <body>
            <div id="app" class="app pt-0">
                <div class="daily-report-wrap">
                    <!-- BEGIN daily-report 1 page -->
                    <div class="daily-report">
                        <div class="daily-sub-page">
                            <!-- brand logo -->
                            <div class="sub-content brand">
                                <div class="brand-logo">
                                    <img src="/Users/aidoi/X-Factor/static/css/reportPageStyle/images/XFactor_logo.png" alt="x-factor로고">
                                </div>
                                <p class="brand-title">자산 리포트</p>
                            </div>
                            <!-- daily-report-content -->
                            <div class="sub-content daily-report-content">
                                <div class="daily-report-content-right">
                                    <div class="daily-report-logo">
                                        <img src="/Users/aidoi/X-Factor/static/css/reportPageStyle/images/Tanium_logo.png" alt="Tanium로고">
                                    </div>
                                    <p class="daily-report-text">
                                        일간 자산 리포트
                                    </p>
                                </div>
                                <div class="daily-report-content-left">
                                    <ul>
                                        <li>
                                            <p>리포트 생성일</p>
                                            <p>2022-09-28</p>
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
            </div>
            <script src='http://"""+libUrl+""":"""+libPort+"""/static/js/jquery/jquery-3.6.0.min.js'></script>
            <script src='http://"""+libUrl+""":"""+libPort+"""/static/assets/plugins/bootstrap/dist/js/bootstrap.min.js'></script>
            <script src='http://"""+libUrl+""":"""+libPort+"""/static/assets/js/vendor.min.js'></script>
            <script src='http://"""+libUrl+""":"""+libPort+"""/static/assets/js/app.min.js'></script>
            <!-- apexchart -->
            <script src='http://"""+libUrl+""":"""+libPort+"""/static/assets/plugins/apexcharts/dist/apexcharts.min.js'></script>
            <script src='/Users/aidoi/X-Factor/static/js/reportPageJS/reportPage_dailyChart.js'></script>
            </body>
            </html>
    """
    with open('html_file.html', 'w', encoding="UTF-8") as html_file:
        html_file.write(html_text)