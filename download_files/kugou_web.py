#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author@zhaopeng
# @time: 2023/6/12 13:28

import requests
from bs4 import BeautifulSoup

url = "https://www.kugou.com/ts/album/16kzygab/p1.html"

payload = {}
headers = {
    'authority': 'www.kugou.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': 'kg_mid=0a3df919e29a5222c3a112fd0fcd91b3; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1686288424; kg_dfid=1twuST2NT6jC0r1mYJ0wSQMA; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22gzlogin-user.kugou.com%22%5D%5D%7D; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1686547582',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
}

# response = requests.request("GET", url, headers=headers, data=payload)
# print(response.text)

a = """

<!DOCTYPE html>
<html>



<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="dns-prefetch" href="//static.kgimg.com/">
    <link rel="dns-prefetch" href="//sdn.kugou.com/">
    <title>虚空凝剑行有声小说-阿伦-有声小说mp3在线收听-酷狗听书</title>
    <meta name="keywords" content="虚空凝剑行,虚空凝剑行在线听,虚空凝剑行有声小说" />
    <meta name="description" content="为什么修仙、修魔、修妖、修佛甚至是修神都要有境界的约束呢？？
酷狗听书为您更新了最新的虚空凝剑行，听书，就来酷狗听书！" />
    <link href="https://www.kugou.com/yy/static/images/favicon.ico" rel="shortcut icon" />
    <link rel="stylesheet" href="/ts/Public/static/css/ts_common.css">
    <link rel="stylesheet" href="/ts/Public/static/css/ts_album.css">
</head>


<body>
<!-- pc部分 -->
<div class="ts_pc" style="display: block;">
<!-- 头部 -->


<script>
  // ie9及以下 提示升级浏览器
  var checkIe9 = function() {
    function IEVersion () {
      if (document.documentMode) return document.documentMode;
    }
    if (IEVersion()) {
      if (IEVersion() <= 9) {
        document.body.innerHTML = ('<p style="position:absolute;width:100%;height:100%;background:#fff;z-index:99999999;left:0;top:0;font-size: 30px;text-align: center;color: #00A9FF;">您的浏览器版本过低，可能存在安全风险，建议升级或更换浏览器后浏览本站</p>')
      }
    } else {
    }
  }
  checkIe9()
</script>
<link rel="stylesheet" href="https://www.kugou.com/common/css/cmdialog.css?20220113">
<link rel="stylesheet" href="https://www.kugou.com/common/css/cmhead.css?20220113">
<div class="cmhead1" >
    <div class="cmhead1_d0">
        <div class="cmhead1_d1">
            <a href="https://www.kugou.com" class="cmhead1_a2">
                <img src="https://www.kugou.com/common/images/kugou_white.png" alt="" class="cmhead1_i1">
            </a>
            <div class="cmhead1_d7">
                <div class="cmhead1_nd0"></div>
                <div class="cmhead1_nd1 _nfCon"></div>
                <input type="text" class="cmhead1_ipt1 _cmheadsearchinput" />
                <div class="cmhead1_d8 _searchbtn4cmhead"></div>
                <div class="cmhead1_d12 _recommend4cmhead">
                    <ul class="cmhead1_ul1 _recommendsong">
                    </ul>
                    <div class="cmhead1_d13">
                        <span class="cmhead1_sp2"></span>
                        <span class="cmhead1_sp3">MV</span>
                    </div>
                    <ul class="cmhead1_ul1 _recommendmv">
                    </ul>
                </div>
                <div class="cmhead1_d14 _history4cmhead">
                    <ul class="cmhead1_ul1 _historysong">
                    </ul>
                    <div class="cmhead1_d15 _clearhistorysong">清空搜索历史</div>
                </div>
            </div>
        </div>
        <div class="cmhead1_d2">
            <a target="_blank" href="https://www.kugou.com/imusic/" target="_blank" class="cmhead1_a1">音乐人</a>
            <a target="_blank" href="http://www.kugou.com/fmugc-v2/dist/index.html" target="_blank" class="cmhead1_a1" rel="nofollow">音频创作</a>
            <a target="_blank" href="http://vip.kugou.com/" target="_blank" class="cmhead1_a1" rel="nofollow">VIP会员</a>

            <div class="cmhead1_d3"></div>

            <div class="cmhead1_d4">
                <div class="cmhead1_d5 _login">登录</div>
                <div class="cmhead1_d6 _userinfoBox">
                    <div class="cmhead1_d9">
                        <img src="" alt="" class="cmhead1_i2">
                        <span class="cmhead1_sp1"></span>
                    </div>
                    <div class="cmhead1_d10">
                        <a class="cmhead1_d11 _userinfo" target="_blank" href="https://www.kugou.com/newuc/user/uc/type=edit" rel="nofollow">个人帐号</a>
                        <a class="cmhead1_d11 _logout" href="https://www.kugou.com/newuc/login/outlogin" rel="nofollow">退出登录</a>
                    </div>
                </div>
            </div>
        </div>

    </div>
    
</div>
<div class="cmhead2" >
    <div class="cmhead2_d0"></div>
    <div class="cmhead2_d01"></div>
    <ul class="cmhead2_ul1">
        <li class="cmhead2_li1">
            <a href="https://www.kugou.com/" class="cmhead2_a1">首页</a>
        </li>
        <li class="cmhead2_li1" id="_rankhome">
            <a href="https://www.kugou.com/yy/html/rank.html" class="cmhead2_a1">榜单</a>
        </li>
        <li class="cmhead2_li1" id="_tshome">
            <a href="https://www.kugou.com/ts/" class="cmhead2_a1">听书</a>
        </li>
        <li class="cmhead2_li1">
            <a href="http://fanxing.kugou.com/?action=spreadIndex&id=3" target="_blank" class="cmhead2_a1">直播</a>
        </li>
        <li class="cmhead2_li1">
            <a href="https://kugou.tmall.com/" target="_blank" class="cmhead2_a1">商城</a>
        </li>
        <li class="cmhead2_li1" id="_downloadhome">
            <a href="https://download.kugou.com/" class="cmhead2_a1">下载酷狗</a>
        </li>
        <li class="cmhead2_li1" >
            <a href="https://www.kugou.com/about/business.html" class="cmhead2_a1">商务合作</a>
        </li>
        <li class="cmhead2_li1 _more">
            <div class="cmhead2_d2">
                更多
                <div class="cmhead2_d3"></div>
            </div>
            <ul class="cmhead2_ul2">
                <li style="
                    height: 15px;
                    margin-top: -25px;
                    position: absolute;
                    width: 100%;
                "></li>
                <li class="cmhead2_li2">
                    <a href="https://www.kugou.com/fmweb/html/index.html" class="cmhead2_a2">频道</a>
                </li>
                <li class="cmhead2_li2">
                    <a href="https://www.kugou.com/mvweb/html/" class="cmhead2_a2">MV</a>
                </li>
                <li class="cmhead2_li2">
                    <a href="https://www.kugou.com/yy/html/special.html" class="cmhead2_a2">歌单</a>
                </li>
                <li class="cmhead2_li2">
                    <a href="https://www.kugou.com/yy/html/singer.html" class="cmhead2_a2">歌手</a>
                </li>
                <li class="cmhead2_li2">
                    <a href="https://www.kugou.com/yy/album/index/1-1-1.html" class="cmhead2_a2">专辑</a>
                </li>
            </ul>
        </li>
    </ul>
</div>
<script src="https://m.kugou.com/static/js/share/npm/sentry5.6.1.min.js" crossorigin="anonymous"></script>
<script>
    Sentry.init({
        dsn: "https://fc8678a0071145128f0c8314c07f8407@sentry.kugou.com/33",
        // integrations: [new Sentry.Integrations.BrowserTracing()],
        sampleRate: 0.1,
    })
</script>

<script type="text/javascript" src="https://www.kugou.com/common/js/jquery.min.js"></script>
<script type="text/javascript" src="https://www.kugou.com/common/js/lib.js"></script>
<script type="text/javascript" src="https://www.kugou.com/common/js/utility.js"></script>
<script src="https://staticssl.kugou.com/common/js/min/login/kguser.v2.min.js?20190111"></script>
<script src="https://staticssl.kugou.com/common/js/repalceHttpsImg.js"></script>
<script src="https://staticssl.kugou.com/common/js/min/npm/getBaseInfo.min.js"></script>
<script src="https://staticssl.kugou.com/common/js/min/infSign.min.js"></script>
<script type="text/javascript" src="https://staticssl.kugou.com/verify/static/js/registerDev.v1.min.js?appid=1014&20190408" charset="utf-8"></script>
<script type="text/javascript" src="https://www.kugou.com/common/js/cmhead.min.js?20220119"></script>

<div class="ts_comm_wrap">
    <div class="ts_comm_nav">
        <span class="ts_comm_nav_sp1">我的位置:</span>
        <a href="/" class="ts_comm_nav_a1">首页</a>
        <span class="ts_comm_nav_sp2">></span>
        <a href="/ts/" class="ts_comm_nav_a1">听书</a>
        <span class="ts_comm_nav_sp2">></span>
        <a href="/ts/xiaoshuo" class="ts_comm_nav_a1">有声小说</a>        <span class="ts_comm_nav_sp2">></span>
        <a href="/ts/category/906-1023/" class="ts_comm_nav_a1">武侠仙侠</a>        <span class="ts_comm_nav_sp2">></span>
        <span class="ts_comm_nav_sp3">虚空凝剑行</span>
    </div>
    <div class="ts_comm_main">
        <div class="ts_comm_info">
            <div class="ts_comm_info_d1">
                <img src="https://imgessl.kugou.com/stdmusic/150/20230410/20230410141515276219.jpg" alt="虚空凝剑行" />
                <span>1.3万</span>
            </div>
            <div class="ts_comm_info_d2">
                <div class="ts_comm_info_d2_d1">
                                        <h3 class="ts_comm_info_d2_d1_h31">虚空凝剑行</h3>
                </div>
                <div class="ts_comm_info_d2_d2">
                    <span class="ts_comm_info_d2_d2_sp1">1.3万</span>
                </div>
                <div class="ts_comm_info_d2_d3">
                    <a href="javascript:;" style="cursor: default;">2023年06月更新</a>                    <a href="/ts/category/906-1023/">武侠仙侠</a>                </div>
                <div class="ts_comm_info_d2_d4">
                    <span class="ts_comm_info_d2_d4_sp1">播放全部</span>
                </div>
            </div>
        </div>
        <div class="tsa_d2">
            <span class="tsa_d2_sp1">内容介绍</span>
            <p class="tsa_d2_p1 _singerIntro _si2">
                为什么修仙、修魔、修妖、修佛甚至是修神都要有境界的约束呢？？
什么境界的约束？全是狗屁，我只追求力量，只要力量达到了，境界自然会自己上去            </p>
        </div>
        <div class="tsa_d3">
            <div class="tsa_d3_d1">
                <div class="tsa_d3_d1_d1">
                    <span class="tsa_d3_d1_d1_sp1">专辑</span>
                    <span class="tsa_d3_d1_d1_sp2">(1232)</span>
                </div>
                <div class="tsa_d3_d1_d2">
                    <span class="tsa_d3_d1_d2_sp1 current"><a style="color: inherit" href="/ts/album/16kzygab/">正序</a></span>
                    <span class="tsa_d3_d1_d2_sp2"></span>
                    <span class="tsa_d3_d1_d2_sp3 "><a style="color: inherit" href="/ts/album/16kzygab/p1-1.html">倒序</a></span>
                </div>
            </div>
            <div class="tsa_d3_d2">
                <ul class="tsa_d3_d2_ul">
                    <li class="tsa_d3_d2_li" data-hash="4470AB4D29F0A8BC8D398E3299C9533E" data-album_id="71523592" data-album_audio_id="503129263" data-encode_album_audio_id="8bjt0v20">
                        <div class="tsa_d3_d2_li_d1">
                            <i data-index=0></i>
                            <span><a style="color: inherit" href="/ts/album/16kzygab/8bjt0v20.html">虚空凝剑行 第1集</a></span>
                        </div>
                        <div class="tsa_d3_d2_li_d2">
                            <span>247</span>
                            <span>08:22</span>
                        </div>
                    </li><li class="tsa_d3_d2_li" data-hash="7A433AC3702AC616DFDDA2CC586AE5BD" data-album_id="71523592" data-album_audio_id="503129535" data-encode_album_audio_id="8bjt8f5b">
                        <div class="tsa_d3_d2_li_d1">
                            <i data-index=1></i>
                            <span><a style="color: inherit" href="/ts/album/16kzygab/8bjt8f5b.html">虚空凝剑行 第2集</a></span>
                        </div>
                        <div class="tsa_d3_d2_li_d2">
                            <span>106</span>
                            <span>06:38</span>
                        </div>
                    </li><li class="tsa_d3_d2_li" data-hash="5AB0FEB47F0C3D6E7B1234CC75B79C62" data-album_id="71523592" data-album_audio_id="503128968" data-encode_album_audio_id="8bjsso7e">
                        <div class="tsa_d3_d2_li_d1">
                            <i data-index=2></i>
                            <span><a style="color: inherit" href="/ts/album/16kzygab/8bjsso7e.html">虚空凝剑行 第3集</a></span>
                        </div>
                        <div class="tsa_d3_d2_li_d2">
                            <span>86</span>
                            <span>07:58</span>
                        </div>
                    </li><li class="tsa_d3_d2_li" data-hash="7371BC6690EEF4B9982DBA1BCEC0B0A7" data-album_id="71523592" data-album_audio_id="503129633" data-encode_album_audio_id="8bjtb5d3">
                        <div class="tsa_d3_d2_li_d1">
                            <i data-index=3></i>
                            <span><a style="color: inherit" href="/ts/album/16kzygab/8bjtb5d3.html">虚空凝剑行 第4集</a></span>
                        </div>
                        <div class="tsa_d3_d2_li_d2">
                            <span>75</span>
                            <span>08:10</span>
                        </div>
                    </li><li class="tsa_d3_d2_li" data-hash="73CE6D8F6C76AC1507F7DCD8577B3F1C" data-album_id="71523592" data-album_audio_id="503129880" data-encode_album_audio_id="8bjti01e">
                        <div class="tsa_d3_d2_li_d1">
                            <i data-index=4></i>
                            <span><a style="color: inherit" href="/ts/album/16kzygab/8bjti01e.html">虚空凝剑行 第5集</a></span>
                        </div>
                        <div class="tsa_d3_d2_li_d2">
                            <span>71</span>
                            <span>07:30</span>
                        </div>
                    </li><li class="tsa_d3_d2_li" data-hash="AA7BE1A7D926433F8D3C792A63D9AE52" data-album_id="71523592" data-album_audio_id="503129774" data-encode_album_audio_id="8bjtf297">
                        <div class="tsa_d3_d2_li_d1">
                            <i data-index=5></i>
                            <span><a style="color: inherit" href="/ts/album/16kzygab/8bjtf297.html">虚空凝剑行 第6集</a></span>
                        </div>
                        <div class="tsa_d3_d2_li_d2">
                            <span>67</span>
                            <span>07:46</span>
                        </div>
                    </li><li class="tsa_d3_d2_li" data-hash="479D42D0C0611AB71DBB963F612C18A1" data-album_id="71523592" data-album_audio_id="503130144" data-encode_album_audio_id="8bjtpc3c">
                        <div class="tsa_d3_d2_li_d1">
                            <i data-index=6></i>
                            <span><a style="color: inherit" href="/ts/album/16kzygab/8bjtpc3c.html">虚空凝剑行 第7集</a></span>
                        </div>
                        <div class="tsa_d3_d2_li_d2">
                            <span>64</span>
                            <span>08:06</span>
                        </div>
                    </li><li class="tsa_d3_d2_li" data-hash="2A87F82652A7937025888EEC59BAFB55" data-album_id="71523592" data-album_audio_id="503129903" data-encode_album_audio_id="8bjtineb">
                        <div class="tsa_d3_d2_li_d1">
                            <i data-index=7></i>
                            <span><a style="color: inherit" href="/ts/album/16kzygab/8bjtineb.html">虚空凝剑行 第8集</a></span>
                        </div>
                        <div class="tsa_d3_d2_li_d2">
                            <span>60</span>
                            <span>08:06</span>
                        </div>
                    </li><li class="tsa_d3_d2_li" data-hash="5DD53378D4388EC1B3A5EF62CF259137" data-album_id="71523592" data-album_audio_id="503130119" data-encode_album_audio_id="8bjton26">
                        <div class="tsa_d3_d2_li_d1">
                            <i data-index=8></i>
                            <span><a style="color: inherit" href="/ts/album/16kzygab/8bjton26.html">虚空凝剑行 第9集</a></span>
                        </div>
                        <div class="tsa_d3_d2_li_d2">
                            <span>60</span>
                            <span>07:56</span>
                        </div>
                    </li><li class="tsa_d3_d2_li" data-hash="48D685529FCDCF5B88BE19DDBD0B5843" data-album_id="71523592" data-album_audio_id="503130415" data-encode_album_audio_id="8bjtwvf7">
                        <div class="tsa_d3_d2_li_d1">
                            <i data-index=9></i>
                            <span><a style="color: inherit" href="/ts/album/16kzygab/8bjtwvf7.html">虚空凝剑行 第10集</a></span>
                        </div>
                        <div class="tsa_d3_d2_li_d2">
                            <span>54</span>
                            <span>08:14</span>
                        </div>
                    </li><li class="tsa_d3_d2_li" data-hash="C042B532B1C07AC8BDE72E4088CB9928" data-album_id="71523592" data-album_audio_id="503130456" data-encode_album_audio_id="8bjty0e4">
                        <div class="tsa_d3_d2_li_d1">
                            <i data-index=10></i>
                            <span><a style="color: inherit" href="/ts/album/16kzygab/8bjty0e4.html">虚空凝剑行 第11集</a></span>
                        </div>
                        <div class="tsa_d3_d2_li_d2">
                            <span>51</span>
                            <span>07:13</span>
                        </div>
                    </li><li class="tsa_d3_d2_li" data-hash="B9C0FB0ED5322D6DC03A1B6B05EC3274" data-album_id="71523592" data-album_audio_id="503129712" data-encode_album_audio_id="8bjtdca6">
                        <div class="tsa_d3_d2_li_d1">
                            <i data-index=11></i>
                            <span><a style="color: inherit" href="/ts/album/16kzygab/8bjtdca6.html">虚空凝剑行 第12集</a></span>
                        </div>
                        <div class="tsa_d3_d2_li_d2">
                            <span>50</span>
                            <span>07:40</span>
                        </div>
                    </li><li class="tsa_d3_d2_li" data-hash="F775F5E5F81E76C837ECBD05356C3726" data-album_id="71523592" data-album_audio_id="503130330" data-encode_album_audio_id="8bjtui30">
                        <div class="tsa_d3_d2_li_d1">
                            <i data-index=12></i>
                            <span><a style="color: inherit" href="/ts/album/16kzygab/8bjtui30.html">虚空凝剑行 第13集</a></span>
                        </div>
                        <div class="tsa_d3_d2_li_d2">
                            <span>49</span>
                            <span>07:31</span>
                        </div>
                    </li><li class="tsa_d3_d2_li" data-hash="78E0D293F664979A18EDC78A38EA41C5" data-album_id="71523592" data-album_audio_id="503130840" data-encode_album_audio_id="8bju8odc">
                        <div class="tsa_d3_d2_li_d1">
                            <i data-index=13></i>
                            <span><a style="color: inherit" href="/ts/album/16kzygab/8bju8odc.html">虚空凝剑行 第14集</a></span>
                        </div>
                        <div class="tsa_d3_d2_li_d2">
                            <span>48</span>
                            <span>07:22</span>
                        </div>
                    </li><li class="tsa_d3_d2_li" data-hash="06F4D1580DF0EF47562F6B54F39FB71C" data-album_id="71523592" data-album_audio_id="503129752" data-encode_album_audio_id="8bjtegea">
                        <div class="tsa_d3_d2_li_d1">
                            <i data-index=14></i>
                            <span><a style="color: inherit" href="/ts/album/16kzygab/8bjtegea.html">虚空凝剑行 第15集</a></span>
                        </div>
                        <div class="tsa_d3_d2_li_d2">
                            <span>47</span>
                            <span>06:59</span>
                        </div>
                    </li><li class="tsa_d3_d2_li" data-hash="C945D9441FB4B0DB5F786C9C41FB9B25" data-album_id="71523592" data-album_audio_id="503130706" data-encode_album_audio_id="8bju4y80">
                        <div class="tsa_d3_d2_li_d1">
                            <i data-index=15></i>
                            <span><a style="color: inherit" href="/ts/album/16kzygab/8bju4y80.html">虚空凝剑行 第16集</a></span>
                        </div>
                        <div class="tsa_d3_d2_li_d2">
                            <span>47</span>
                            <span>07:05</span>
                        </div>
                    </li><li class="tsa_d3_d2_li" data-hash="AD7F18E7EAFF651EA7861BE31898730F" data-album_id="71523592" data-album_audio_id="503130412" data-encode_album_audio_id="8bjtws6d">
                        <div class="tsa_d3_d2_li_d1">
                            <i data-index=16></i>
                            <span><a style="color: inherit" href="/ts/album/16kzygab/8bjtws6d.html">虚空凝剑行 第17集</a></span>
                        </div>
                        <div class="tsa_d3_d2_li_d2">
                            <span>46</span>
                            <span>07:32</span>
                        </div>
                    </li><li class="tsa_d3_d2_li" data-hash="A3C00DA1218F8F49CFE8AC94B53358E4" data-album_id="71523592" data-album_audio_id="503130350" data-encode_album_audio_id="8bjtv28d">
                        <div class="tsa_d3_d2_li_d1">
                            <i data-index=17></i>
                            <span><a style="color: inherit" href="/ts/album/16kzygab/8bjtv28d.html">虚空凝剑行 第18集</a></span>
                        </div>
                        <div class="tsa_d3_d2_li_d2">
                            <span>46</span>
                            <span>07:38</span>
                        </div>
                    </li><li class="tsa_d3_d2_li" data-hash="7F6907DB6EBFA109BA6B41FC99617D77" data-album_id="71523592" data-album_audio_id="503130155" data-encode_album_audio_id="8bjtpn78">
                        <div class="tsa_d3_d2_li_d1">
                            <i data-index=18></i>
                            <span><a style="color: inherit" href="/ts/album/16kzygab/8bjtpn78.html">虚空凝剑行 第19集</a></span>
                        </div>
                        <div class="tsa_d3_d2_li_d2">
                            <span>43</span>
                            <span>07:29</span>
                        </div>
                    </li><li class="tsa_d3_d2_li" data-hash="" data-album_id="71523592" data-album_audio_id="503129790" data-encode_album_audio_id="8bjtfi9c">
                        <div class="tsa_d3_d2_li_d1">
                            <i data-index=19></i>
                            <span><a style="color: inherit" href="/ts/album/16kzygab/8bjtfi9c.html">虚空凝剑行 第20集</a></span>
                        </div>
                        <div class="tsa_d3_d2_li_d2">
                            <span>47</span>
                            <span>07:59</span>
                        </div>
                    </li>                </ul>
                <div id="page"></div>
            </div>
        </div>
    </div>
    <div class="ts_comm_side">
        <h2 class="tscomm_t_h2">
            主<span class="tscomm_t_sp1">播</span>
        </h2>
        <div class="tsas_d1">
            <div class="tsas_d1_d1">
                <img class="tsas_d1_d1_img1" src="https://imgessl.kugou.com/uploadpic/softhead/150/20220609/20220609100753807783.jpg" alt="" />
                <div class="tsas_d1_d1_d1">
                    <a class="tsas_d1_d1_d1_sp1" href="/ts/zhubo/59kb7db/">阿伦</a>
                    
                    <p class="tsas_d1_d1_d1_p1">
                        <span class="tsas_d1_d1_d1_p1_sp1">2402粉丝</span>
                        <span class="tsas_d1_d1_d1_p1_sp2">729专辑</span>
                    </p>
                </div>
            </div>
            <p class="tsas_d1_p1 _singerIntro _si1">
                阿伦，有声小说主播。            </p>
        </div>
        <div class="tsas_d2">
            <div class="tscomm_title">
                <h2 class="tscomm_t_h2">
                    TA<span class="tscomm_t_sp1">的作品</span>
                </h2>
                
                 <span class="tscomm_t_sp2"><a href="/ts/zhubo/59kb7db/" style="text-decoration: none;color: inherit">更多</a></span>            </div>
            <ul class="ts_comm_item2_ul">
                <li class="ts_comm_item2_li">
                        <a href="/ts/album/17vrnkfd" class="ts_comm_item2_a1">
                            <img src="https://imgessl.kugou.com/stdmusic/150/20230523/20230523161513156723.jpg" alt="万古仙尊" class="ts_comm_item2_i1">
                            <div class="ts_comm_item2_d1">
                                1494                            </div>
                        </a>
                        <div class="ts_comm_item2_d2">
                            <a href="/ts/album/17vrnkfd/" class="ts_comm_item2_a2">万古仙尊</a>
                            <a href="/ts/zhubo/59kb7db/" class="ts_comm_item2_a3">阿伦</a>
                        </div>

                    </li><li class="ts_comm_item2_li">
                        <a href="/ts/album/17kghjf0" class="ts_comm_item2_a1">
                            <img src="https://imgessl.kugou.com/stdmusic/150/20230512/20230512181707911014.jpg" alt="陈二狗修道记丨算命阴阳道法" class="ts_comm_item2_i1">
                            <div class="ts_comm_item2_d1">
                                1.2万                            </div>
                        </a>
                        <div class="ts_comm_item2_d2">
                            <a href="/ts/album/17kghjf0/" class="ts_comm_item2_a2">陈二狗修道记丨算命阴阳道法</a>
                            <a href="/ts/zhubo/59kb7db/" class="ts_comm_item2_a3">阿伦</a>
                        </div>

                    </li><li class="ts_comm_item2_li">
                        <a href="/ts/album/17khu934" class="ts_comm_item2_a1">
                            <img src="https://imgessl.kugou.com/stdmusic/150/20230512/20230512182026711328.jpg" alt="穿越之科技王朝" class="ts_comm_item2_i1">
                            <div class="ts_comm_item2_d1">
                                4723                            </div>
                        </a>
                        <div class="ts_comm_item2_d2">
                            <a href="/ts/album/17khu934/" class="ts_comm_item2_a2">穿越之科技王朝</a>
                            <a href="/ts/zhubo/59kb7db/" class="ts_comm_item2_a3">阿伦</a>
                        </div>

                    </li>            </ul>
        </div>        <div class="tsas_d3">
            <div class="tscomm_title">
                <h2 class="tscomm_t_h2">
                    相关<span class="tscomm_t_sp1">推荐</span>
                </h2>
            </div>
                        <ul class="ts_comm_item2_ul">
                <li class="ts_comm_item2_li">
                        <a href="/ts/album/10vobe98/" class="ts_comm_item2_a1">
                            <img src="https://imgessl.kugou.com/stdmusic/150/20221019/20221019073603735336.jpg" alt="仙路争锋" class="ts_comm_item2_i1">
                            <div class="ts_comm_item2_d1">
                                                            </div>
                        </a>
                        <div class="ts_comm_item2_d2">
                            <a href="/ts/album/10vobe98/" class="ts_comm_item2_a2">仙路争锋</a>
                            <!--<a href="" class="ts_comm_item2_a3"></a>-->
                        </div>

                    </li><li class="ts_comm_item2_li">
                        <a href="/ts/album/16e9es18/" class="ts_comm_item2_a1">
                            <img src="https://imgessl.kugou.com/stdmusic/150/20230404/20230404121542498854.jpg" alt="混沌雷修" class="ts_comm_item2_i1">
                            <div class="ts_comm_item2_d1">
                                                            </div>
                        </a>
                        <div class="ts_comm_item2_d2">
                            <a href="/ts/album/16e9es18/" class="ts_comm_item2_a2">混沌雷修</a>
                            <!--<a href="" class="ts_comm_item2_a3"></a>-->
                        </div>

                    </li><li class="ts_comm_item2_li">
                        <a href="/ts/album/16r61ra2/" class="ts_comm_item2_a1">
                            <img src="https://imgessl.kugou.com/stdmusic/150/20230413/20230413143321326005.jpg" alt="太易" class="ts_comm_item2_i1">
                            <div class="ts_comm_item2_d1">
                                                            </div>
                        </a>
                        <div class="ts_comm_item2_d2">
                            <a href="/ts/album/16r61ra2/" class="ts_comm_item2_a2">太易</a>
                            <!--<a href="" class="ts_comm_item2_a3"></a>-->
                        </div>

                    </li><li class="ts_comm_item2_li">
                        <a href="/ts/album/15z6fa32/" class="ts_comm_item2_a1">
                            <img src="https://imgessl.kugou.com/stdmusic/150/20230323/20230323132122705048.jpg" alt="仙傲" class="ts_comm_item2_i1">
                            <div class="ts_comm_item2_d1">
                                                            </div>
                        </a>
                        <div class="ts_comm_item2_d2">
                            <a href="/ts/album/15z6fa32/" class="ts_comm_item2_a2">仙傲</a>
                            <!--<a href="" class="ts_comm_item2_a3"></a>-->
                        </div>

                    </li><li class="ts_comm_item2_li">
                        <a href="/ts/album/qv3av43/" class="ts_comm_item2_a1">
                            <img src="https://imgessl.kugou.com/stdmusic/150/20201119/20201119203601547667.jpg" alt="气冲星河" class="ts_comm_item2_i1">
                            <div class="ts_comm_item2_d1">
                                                            </div>
                        </a>
                        <div class="ts_comm_item2_d2">
                            <a href="/ts/album/qv3av43/" class="ts_comm_item2_a2">气冲星河</a>
                            <!--<a href="" class="ts_comm_item2_a3"></a>-->
                        </div>

                    </li><li class="ts_comm_item2_li">
                        <a href="/ts/album/15xv9z9f/" class="ts_comm_item2_a1">
                            <img src="https://imgessl.kugou.com/stdmusic/150/20230321/20230321181638944497.jpg" alt="法相仙途" class="ts_comm_item2_i1">
                            <div class="ts_comm_item2_d1">
                                                            </div>
                        </a>
                        <div class="ts_comm_item2_d2">
                            <a href="/ts/album/15xv9z9f/" class="ts_comm_item2_a2">法相仙途</a>
                            <!--<a href="" class="ts_comm_item2_a3"></a>-->
                        </div>

                    </li><li class="ts_comm_item2_li">
                        <a href="/ts/album/tx08n58/" class="ts_comm_item2_a1">
                            <img src="https://imgessl.kugou.com/stdmusic/150/20210930/20210930161400230580.jpg" alt="飞剑问道" class="ts_comm_item2_i1">
                            <div class="ts_comm_item2_d1">
                                                            </div>
                        </a>
                        <div class="ts_comm_item2_d2">
                            <a href="/ts/album/tx08n58/" class="ts_comm_item2_a2">飞剑问道</a>
                            <!--<a href="" class="ts_comm_item2_a3"></a>-->
                        </div>

                    </li><li class="ts_comm_item2_li">
                        <a href="/ts/album/zces49e/" class="ts_comm_item2_a1">
                            <img src="https://imgessl.kugou.com/stdmusic/150/20220719/20220719130150127778.jpg" alt="一世之尊" class="ts_comm_item2_i1">
                            <div class="ts_comm_item2_d1">
                                                            </div>
                        </a>
                        <div class="ts_comm_item2_d2">
                            <a href="/ts/album/zces49e/" class="ts_comm_item2_a2">一世之尊</a>
                            <!--<a href="" class="ts_comm_item2_a3"></a>-->
                        </div>

                    </li>            </ul>
        </div>    </div>
</div>

<!--底部-->
<link rel="stylesheet" href="https://www.kugou.com/common/css/cmfoot.css?20220127" />
<div class="cmfoot">
    <ul class="cmfoot_ul1">
        <li class="cmfoot_li1">
            <a href="https://www.tencentmusic.com/" target="_blank" class="cmfoot_a1 _a4i1" rel="nofollow">
                <div class="cmfoot_a1_d1 _i1"></div>
                <p class="cmfoot_a1_p1">腾讯音乐娱乐集团</p>
            </a>
        </li>
        <li class="cmfoot_li1">
            <a href="https://y.tencentmusic.com/" target="_blank" class="cmfoot_a1 _a4i2" rel="nofollow">
                <div class="cmfoot_a1_d1 _i2"></div>
                <p class="cmfoot_a1_p1">腾讯音乐人</p>
            </a>
        </li>
        <li class="cmfoot_li1">
            <a href="https://www.kugou.com/imusic/" target="_blank" class="cmfoot_a1 _a4i3" rel="nofollow">
                <div class="cmfoot_a1_d1 _i3"></div>
                <p class="cmfoot_a1_p1">酷狗音乐人</p>
            </a>
        </li>
        <li class="cmfoot_li1">
            <a href="https://tui.kugou.com/" target="_blank" class="cmfoot_a1 _a4i4" rel="nofollow">
                <div class="cmfoot_a1_d1 _i4"></div>
                <p class="cmfoot_a1_p1">星曜推歌</p>
            </a>
        </li>
        <li class="cmfoot_li1">
            <a href="http://5sing.kugou.com/" target="_blank" class="cmfoot_a1 _a4i5" rel="nofollow">
                <div class="cmfoot_a1_d1 _i5"></div>
                <p class="cmfoot_a1_p1">5sing原创音乐</p>
            </a>
        </li>
        <li class="cmfoot_li1">
            <a href="https://www.kugou.com/music_recognition/?from=pcweb" target="_blank" class="cmfoot_a1 _a4i7" rel="nofollow">
                <div class="cmfoot_a1_d1 _i7"></div>
                <p class="cmfoot_a1_p1">听歌识曲</p>
            </a>
        </li>
        <li class="cmfoot_li1">
            <a href="https://gejigeji.kugou.com/" target="_blank" class="cmfoot_a1 _a4i8">
                <div class="cmfoot_a1_d1 _i8"></div>
                <p class="cmfoot_a1_p1">歌叽歌叽</p>
            </a>
        </li>
    </ul>
    
    <ul class="cmfoot_ul2">
        <li class="cmfoot_li2">
            <a href="https://www.kugou.com/about/aboutus.html" target="_blank" class="cmfoot_a3" rel="nofollow">关于酷狗</a>
        </li>
        <li class="cmfoot_li2">
            <a href="https://www.kugou.com/about/business.html" target="_blank" class="cmfoot_a3" rel="nofollow">商务合作</a>
        </li>
        <li class="cmfoot_li2">
            <a href="https://www.kugou.com/about/adservice.html" target="_blank" class="cmfoot_a3" rel="nofollow">广告服务</a>
        </li>
        <li class="cmfoot_li2">
            <a href="https://www.kugou.com/about/copyRightGuide.html" target="_blank" class="cmfoot_a3" rel="nofollow">投诉指引</a>
        </li>
        <li class="cmfoot_li2">
            <a href="https://activity.kugou.com/privacy4pcweb/v-d45bb170/index.html" target="_blank" class="cmfoot_a3" rel="nofollow">隐私政策</a>
        </li>
        <li class="cmfoot_li2">
            <a href="https://activity.kugou.com/privacy4pcweb/v-5115fce0/index.html" target="_blank" class="cmfoot_a3" rel="nofollow">儿童隐私政策</a>
        </li>
        <li class="cmfoot_li2">
            <a href="https://activity.kugou.com/privacy4pcweb/v-e010f2d0/index.html" target="_blank" class="cmfoot_a3" rel="nofollow">用户服务协议</a>
        </li>
        <li class="cmfoot_li2">
            <a href="https://www.kugou.com/hr/kugouHr/dist/index.html" target="_blank" class="cmfoot_a3" rel="nofollow">招聘信息</a>
        </li>
        <li class="cmfoot_li2">
            <a href="https://www.kugou.com/shop/help/serviceCenter" class="cmfoot_a3" rel="nofollow">客服中心</a>
        </li>
        <li class="cmfoot_li2">
            <a href="https://www.kugou.com/shop/help/serviceCenter?showlist=1" class="cmfoot_a3" rel="nofollow">举报中心</a>
        </li>
    </ul>
    
    <ul class="cmfoot_ul2">
        <li class="cmfoot_li2">
            <a target="_blank" href="https://www.kugou.com/common/images/%E7%BD%91%E7%BB%9C%E6%96%87%E5%8C%96%E7%BB%8F%E8%90%A5%E8%AE%B8%E5%8F%AF%E8%AF%81.png" class="cmfoot_a3" rel="nofollow">粤网文（2022）1053-085号</a>
        </li>
        <li class="cmfoot_li2">
            <a target="_blank" href="https://www.kugou.com/common/images/%E4%BF%A1%E6%81%AF%E7%BD%91%E7%BB%9C%E4%BC%A0%E6%92%AD%E8%A7%86%E5%90%AC%E8%8A%82%E7%9B%AE%E8%AE%B8%E5%8F%AF%E8%AF%81.jpg" class="cmfoot_a3" rel="nofollow">网络视听许可证 1910564号</a>
        </li>
        <li class="cmfoot_li2">
            <a target="_blank" href="https://www.kugou.com/common/images/20210615-ICP%E5%A2%9E%E5%80%BC%E7%94%B5%E4%BF%A1%E4%B8%9A%E5%8A%A1%E7%BB%8F%E8%90%A5%E8%AE%B8%E5%8F%AF%E8%AF%81.png" class="cmfoot_a3" rel="nofollow">增值电信业务 粤B2-20060339</a>
        </li>
        <li class="cmfoot_li2">
            <a target="_blank" href="https://beian.miit.gov.cn/" class="cmfoot_a3" rel="nofollow">粤ICP备09017694号</a>
        </li>
    </ul>
    
    <ul class="cmfoot_ul2">
        <li class="cmfoot_li2">
            <a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=44010602000141" class="cmfoot_a3" rel="nofollow">粤公网安备 44030002000001号</a>
        </li>
        <li class="cmfoot_li2">
            <a target="_blank" href="https://www.kugou.com/common/images/%E4%BA%92%E8%81%94%E7%BD%91%E5%AE%97%E6%95%99%E4%BF%A1%E6%81%AF%E6%9C%8D%E5%8A%A1%E8%AE%B8%E5%8F%AF%E8%AF%81.png" class="cmfoot_a3" rel="nofollow">互联网宗教信息服务许可证 粤（2022）0000022</a>
        </li>
        <li class="cmfoot_li2">
            <a target="_blank" href="https://www.kugou.com/common/images/license.jpg" rel="nofollow" class="cmfoot_a3">营业执照</a>
        </li>
    </ul>

    <div class="cmfoot_d1">
        <a target="_blank" href="https://www.12377.cn/" class="cmfoot_d1_a1" rel="nofollow">互联网不良信息举报中心</a>
        <span class="cmfoot_d1_sp1">酷狗不良信息举报邮箱：jubao_music@kugou.net</span>
        <span class="cmfoot_d1_sp1">客服电话：020-29195668（7*24小时热线）</span>
    </div>

    <div class="cmfoot_d1">
        <span class="cmfoot_d1_sp1">Copyright © 2004-2023 KuGou-Inc.All Rights Reserved</span>
    </div>
    
</div>

<!--百度---统计-->
<script>
    var _hmt = _hmt || [];
    (function () {
        
        var _this = this,
            tUrl = location.href,
            reg = /\d+/g,
            ua = navigator.userAgent.toLowerCase(),
            ipad = /ipad/gi.test(ua),
            android = /android|Adr/gi.test(ua),
            iphone = /iphone/gi.test(ua),
            mobileUa = !!ua.match(/AppleWebKit.*Mobile.*/),
            frwrap = /fr=wrap/gi.test(tUrl);
        var bdScriptSrc = 'https://hm.baidu.com/hm.js?aedee6983d4cfc62f509129360d6bb3d'
        if (!frwrap) {
            if (!ipad) {
                if ((android || iphone || mobileUa) && tUrl.indexOf('m.kugou') != -1) { // 手机UA且访问站点位m.kugou.com (听书移动端页面场景)
                    bdScriptSrc = "https://hm.baidu.com/hm.js?c0eb0e71efad9184bda4158ff5385e91"
                }
            }
        }
        
        var hm = document.createElement("script")
        hm.src = bdScriptSrc
        var s = document.getElementsByTagName("script")[0]
        s.parentNode.insertBefore(hm, s)

    })();
    (function () {
        setTimeout(function () {
            var d = document.createElement("script");
            d.src = "https://staticssl.kugou.com/common/js/min/hijacked-min.js";
            document.body.appendChild(d);
        }, 2000);
    })();
</script>
<script>
    (function () {
        setTimeout(function () {
            var d = document.createElement("script");
            d.src = "https://staticssl.kugou.com/collect/common/dist/js/collect-2400.js";
            document.body.appendChild(d);
        }, 0);
    })();
</script>
</div>

<script>
    var curPage ="1" || 1;
    var pageTotal = "1232"
    var pageSize = "20" || 20;
   
</script>
<script src="https://staticssl.kugou.com/public/root/javascripts/jslib/jquery.js"></script>
<script src="https://staticssl.kugou.com/collect/common/dist/js/collect-2400.js"></script>
<script src="https://staticssl.kugou.com/common/js/min/npm/getBaseInfo.min.js"></script>
<script src="https://staticssl.kugou.com/common/js/min/inf_public-min.js"></script>
<script src="https://login-user.kugou.com/v1/kguser_min.js"></script>
<script src="/ts/Public/static/js/player.js"></script>
<script src="/ts/Public/static/js/pager.js"></script>
<script src="/ts/Public/static/js/ts_album.js"></script>
<script>
    // 曝光埋点需求mtp111977 
    var uaType2 = function () {
        var fs = 0;
        var ua = navigator.userAgent.toLowerCase();
        if (ua && ua.search(/spider/i) > -1) {
            if (ua.search(/Baiduspider/i) > -1) {
                fs = "Baiduspider";
            } else if (ua.search(/Bytespider/i) > -1) {
                fs = "Bytespider";
            } else {
                fs = "Otherspider";
            }
        }
        return fs;
    }
    var getQueryString = function (name) {
        var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
        var r = window.location.search.substr(1).match(reg);
        if (r != null) return unescape(r[2]); return null;
    }
    window.getBaseInfo(1014, function (bInfo) {
        var logPar = {
            a: 28448,
            b: '曝光',
            ft: window.location.href.indexOf('m.kugou.com') == -1 ? 'pc' : 'mobile',
            r: '听书列表页',
            userid: bInfo.userid || 0,
            mid: bInfo.mid,
            uuid: bInfo.uuid,
            fo: document.referrer ? document.referrer.substr(0, 200) : '',
            svar1: window.location.href.substr(0, 200),
            svar2: location.origin,
            svar3: navigator.userAgent,
            svar4: getQueryString('hreffrom') || getQueryString('from'),
            svar5: uaType2(),
        }
        newLogCount(30050, logPar)
    })
</script>
</body>

</html>
"""

b = BeautifulSoup(a, "html.parser")
for i in b.select("body div li span a"):
    # print(type(i))
    # print(i)
    print(i.get("href"), i.contents[0])
