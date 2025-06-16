---
layout: post
title:  "Theophylline aptamer"
date:   2024-04-24 00:00:00
author: Linfei Li, Jiali Wang
categories: Aptamer
---
<html>
<head>
  <style>
    /* 全局变量 */
    :root {
      --primary-color: #520049;
      --secondary-color: #f5f5f5;
      --text-color: #333;
      --border-radius: 8px;
      --transition: all 0.3s ease;
      --box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    /* 基础样式 */
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.7;
      color: var(--text-color);
      position: relative;
      font-size: 16px;
      letter-spacing: 0.3px;
    }

    /* 段落样式优化 */
    p {
      margin-bottom: 18px;
      text-align: justify;
      text-justify: inter-word;
    }

    /* 首字母加粗效果 */
    .content-section p:first-of-type::first-letter {
      font-weight: 700;
      font-size: 1.2em;
      color: var(--primary-color);
    }

    /* 小标题样式 */
    .blowheader_box {
      background: linear-gradient(135deg, var(--primary-color), rgba(82, 0, 73, 0.8));
      color: white;
      padding: 12px 20px;
      margin: 30px 0 20px;
      border-radius: var(--border-radius);
      font-size: 18px;
      font-weight: 600;
      position: relative;
      box-shadow: 0 4px 15px rgba(82, 0, 73, 0.2);
      letter-spacing: 0.5px;
    }

    .blowheader_box::before {
      content: '▶';
      margin-right: 10px;
      font-size: 0.9em;
    }

    .blowheader_box::after {
      content: '';
      position: absolute;
      bottom: -8px;
      left: 20px;
      width: 0;
      height: 0;
      border-left: 8px solid transparent;
      border-right: 8px solid transparent;
      border-top: 8px solid var(--primary-color);
    }

    /* 序列样式优化 */
    .sequence {
      font-family: 'Courier New', monospace;
      background: var(--secondary-color);
      padding: 15px 20px;
      border-radius: var(--border-radius);
      margin: 20px 0;
      border-left: 4px solid var(--primary-color);
      font-size: 16px;
      letter-spacing: 1px;
      font-weight: 600;
      color: #2c3e50;
    }

    /* 强调文本样式 */
    .highlight-text {
      background: linear-gradient(120deg, rgba(82, 0, 73, 0.1) 0%, rgba(82, 0, 73, 0.2) 100%);
      padding: 2px 6px;
      border-radius: 4px;
      font-weight: 500;
    }

    /* 上标样式优化 */
    sup {
      font-size: 0.75em;
      vertical-align: super;
      color: var(--primary-color);
      font-weight: 600;
    }

    /* 下标样式优化 */
    sub {
      font-size: 0.8em;
      vertical-align: sub;
      color: #666;
    }

    /* 导航栏样式 */
    .nav-ball {
      position: fixed;
      top: 50%;
      right: 30px;
      transform: translateY(-50%);
      width: 50px;
      height: 50px;
      background: var(--primary-color);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 1000;
      transition: var(--transition);
      box-shadow: 0 4px 15px rgba(82, 0, 73, 0.3);
    }

    .nav-ball:hover {
      transform: translateY(-50%) scale(1.1);
      box-shadow: 0 6px 20px rgba(82, 0, 73, 0.4);
    }

    .nav-ball.active {
      background: rgba(82, 0, 73, 0.9);
    }

    .nav-ball-icon {
      width: 24px;
      height: 24px;
      position: relative;
    }

    .nav-ball-icon span {
      display: block;
      height: 2px;
      width: 16px;
      background: white;
      margin: 3px auto;
      transition: var(--transition);
      border-radius: 1px;
    }

    .nav-ball.active .nav-ball-icon span:nth-child(1) {
      transform: rotate(45deg) translate(4px, 4px);
    }

    .nav-ball.active .nav-ball-icon span:nth-child(2) {
      opacity: 0;
    }

    .nav-ball.active .nav-ball-icon span:nth-child(3) {
      transform: rotate(-45deg) translate(4px, -4px);
    }

    /* 遮罩层样式 */
    .overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.3);
      opacity: 0;
      visibility: hidden;
      transition: var(--transition);
      z-index: 998;
    }

    .overlay.active {
      opacity: 1;
      visibility: visible;
    }

    /* 内容区块样式 */
    .content-section {
      background: white;
      padding: 25px;
      margin-bottom: 30px;
      border-radius: var(--border-radius);
      box-shadow: var(--box-shadow);
    }

    .section-title {
      color: var(--primary-color);
      font-size: 24px;
      margin-bottom: 20px;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--primary-color);
    }

    .subsection-title {
      color: var(--primary-color);
    font-size: 20px;
      margin: 25px 0 15px;
    }

    /* 时间线样式 */
    .timeline {
      position: relative;
      padding: 40px 0;
      margin: 20px 0;
    }

    .timeline::before {
      content: '';
      position: absolute;
      left: 30px;
      top: 0;
      bottom: 0;
      width: 3px;
      background: linear-gradient(to bottom, var(--primary-color), rgba(82, 0, 73, 0.3));
      border-radius: 2px;
    }

    .entry {
      position: relative;
      margin-left: 80px;
      margin-bottom: 40px;
      opacity: 0;
      transform: translateX(30px);
      animation: slideInRight 0.6s ease forwards;
    }

    .entry:nth-child(even) {
      animation-delay: 0.1s;
    }

    .entry:nth-child(odd) {
      animation-delay: 0.2s;
    }

    @keyframes slideInRight {
      to {
        opacity: 1;
        transform: translateX(0);
      }
    }

    .entry::before {
      content: '';
      position: absolute;
      left: -65px;
      top: 10px;
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: var(--primary-color);
      border: 4px solid white;
      box-shadow: 0 0 0 3px var(--primary-color);
      z-index: 10;
      transition: var(--transition);
    }

    .entry:hover::before {
      transform: scale(1.3);
      box-shadow: 0 0 0 6px rgba(82, 0, 73, 0.3);
    }

    .entry .title {
      margin-bottom: 15px;
    }

    .entry .title h3 {
      margin: 0;
      color: var(--primary-color);
      font-size: 18px;
      font-weight: 600;
    }

    .entry .body {
      background: white;
      padding: 20px;
      border-radius: var(--border-radius);
      box-shadow: 0 4px 15px rgba(0,0,0,0.1);
      border-left: 4px solid var(--primary-color);
      transition: var(--transition);
      position: relative;
    }

    .entry .body::before {
      content: '';
      position: absolute;
      left: -12px;
      top: 20px;
      width: 0;
      height: 0;
      border-top: 8px solid transparent;
      border-bottom: 8px solid transparent;
      border-right: 8px solid white;
    }

    .entry:hover .body {
      transform: translateY(-5px);
      box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }

    .entry .body p {
      margin: 0;
      line-height: 1.6;
      color: #555;
    }

    /* 表格样式 */
    .table {
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
      background: white;
      border-radius: var(--border-radius);
      overflow: hidden;
      box-shadow: var(--box-shadow);
    }

    .table th {
      background: var(--primary-color);
      color: white;
      padding: 15px 12px;
      text-align: left;
      font-weight: 600;
      border-bottom: 2px solid rgba(255,255,255,0.1);
    }

    .table td {
      padding: 15px 12px;
      border-bottom: 1px solid #e8e8e8;
      vertical-align: top;
    }

    .table tbody tr:nth-child(even) {
      background: rgba(245, 245, 245, 0.5);
    }

    .table tbody tr:nth-child(odd) {
      background: white;
    }

    .table tr:hover {
      background: rgba(82, 0, 73, 0.05);
      transform: scale(1.002);
      transition: all 0.2s ease;
    }

    .table tbody tr {
      transition: all 0.2s ease;
    }

    .table tbody tr:last-child td {
      border-bottom: none;
    }

    /* 表格中图片的样式 */
    .table td img {
      max-width: 100px;
      height: auto;
      border-radius: 4px;
    }

    /* 图片样式 */
    .img-responsive {
      max-width: 100%;
      height: auto;
      border-radius: var(--border-radius);
      margin: 20px 0;
    }

    /* 引用样式 */
    blockquote {
      border-left: 4px solid var(--primary-color);
      margin: 20px 0;
      padding: 10px 20px;
      background: var(--secondary-color);
      border-radius: 0 var(--border-radius) var(--border-radius) 0;
    }

    /* 结构查看器样式 */
    .structure-viewer {
      margin: 20px 0;
    }

    .viewer-note {
      text-align: right;
      margin-bottom: 10px;
      color: #666;
    }

    .viewer-container {
      display: flex;
      gap: 20px;
      align-items: flex-start;
    }

    .viewer-controls {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .viewer-controls button {
      padding: 8px 16px;
      background: var(--primary-color);
      color: white;
      border: none;
      border-radius: var(--border-radius);
      cursor: pointer;
      transition: var(--transition);
    }

    .viewer-controls button:hover {
      opacity: 0.9;
    }

    /* 序列样式 */
    .sequence {
      font-family: monospace;
      background: var(--secondary-color);
      padding: 10px;
      border-radius: var(--border-radius);
      margin: 15px 0;
    }

    /* 绑定口袋图片样式 */
    .binding-pocket-images {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin: 20px 0;
    }

    /* 信息框样式 */
    .info-box {
      background: var(--secondary-color);
      padding: 15px;
      border-radius: var(--border-radius);
      margin: 20px 0;
    }

    .info-box p {
      margin: 10px 0;
    }

    .info-box a {
      color: var(--primary-color);
    text-decoration: none;
    }

    .info-box a:hover {
      text-decoration: underline;
    }

    /* 结构图片样式 */
    .structure-images {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin: 20px 0;
    }

    .structure-images img {
      width: 100%;
      height: auto;
      border-radius: var(--border-radius);
    }

    /* 链接样式 */
    a {
      color: var(--primary-color);
      text-decoration: none;
      transition: var(--transition);
    }

    a:hover {
      opacity: 0.8;
    }

    /* 表格中的链接样式 */
    .table a {
      color: var(--primary-color);
      font-weight: bold;
    }

    /* 响应式设计 */
    @media (max-width: 768px) {
      .side-nav ul {
        flex-direction: column;
}
      
      .side-nav-item {
        width: 100%;
      }
      
      .side-nav-item a {
    display: block;
      text-align: center;
      }

      .content-section {
        padding: 15px;
  }

      .table {
        display: block;
        overflow-x: auto;
  }

      /* 3D可视化移动端样式 */
      .structure-table {
        width: 100% !important;
        display: block;
        overflow-x: auto;
      }

      .structure-table td {
        display: block;
        width: 100%;
        margin-bottom: 20px;
      }

      .structure-table td img,
      .structure-table #myViewer1 {
        width: 100% !important;
        max-width: 350px;
        height: auto !important;
      }

      .binding-pocket-table {
        width: 100% !important;
        display: block;
        overflow-x: auto;
      }

      .binding-pocket-table td {
        display: block;
        width: 100%;
        margin-bottom: 20px;
      }

      .binding-pocket-table td img {
        width: 100% !important;
        max-width: 350px;
      }

      .viewer-container {
        flex-direction: column;
  }

      .binding-pocket-images {
        grid-template-columns: 1fr;
      }

      .structure-images {
        grid-template-columns: 1fr;
      }

      .info-box {
        padding: 10px;
      }
        }

    /* 3D可视化部分特殊样式 */
    .structure-table {
      margin: 20px auto;
      border-collapse: collapse;
      background: white;
      border-radius: var(--border-radius);
      overflow: hidden;
      box-shadow: var(--box-shadow);
    }

    .structure-table td {
      padding: 0;
      border: none;
      vertical-align: top;
    }

    /* 3D可视化表格中的图片不受尺寸限制 */
    .structure-table td img {
      max-width: none;
      width: 500px;
      height: auto;
    }

    /* Molstar容器样式 */
    .structure-table #myViewer1 {
      width: 500px !important;
      height: 500px !important;
    }

    /* 绑定口袋表格样式 */
    .binding-pocket-table {
      width: 1000px;
      margin: 20px auto;
      border-collapse: collapse;
      background: white;
      border-radius: var(--border-radius);
      overflow: hidden;
      box-shadow: var(--box-shadow);
    }

    .binding-pocket-table td {
      padding: 0;
      border: none;
      text-align: center;
    }

    .binding-pocket-table td img {
      max-width: none;
      width: 500px;
      height: auto;
    }

    /* 侧边导航样式 */
    .side-nav {
      position: fixed !important;
      top: 50% !important;
      right: 90px !important;
      left: auto !important;
      transform: translateY(-50%) scale(0);
      background: rgba(255, 255, 255, 0.95);
      padding: 15px 0;
      border-radius: var(--border-radius);
      box-shadow: 0 5px 20px rgba(0,0,0,0.2);
      z-index: 999;
      transition: transform 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
      backdrop-filter: blur(15px);
      -webkit-backdrop-filter: blur(15px);
      width: 200px;
      max-width: 200px;
      opacity: 0;
    }

    .side-nav.active {
      transform: translateY(-50%) scale(1);
      opacity: 1;
    }

    .side-nav ul {
      list-style: none;
      padding: 0;
      margin: 0;
    }

    .side-nav-item {
      margin: 0;
      position: relative;
    }

    .side-nav-item a {
      display: block;
      padding: 10px 15px;
      color: var(--primary-color);
      text-decoration: none;
      transition: var(--transition);
      font-size: 14px;
      position: relative;
      overflow: hidden;
    }

    .side-nav-item a::before {
      content: '';
      position: absolute;
      left: 0;
      top: 0;
      height: 100%;
      width: 4px;
      background: var(--primary-color);
      transform: scaleY(0);
      transition: transform 0.2s;
    }

    .side-nav-item a:hover {
      background: rgba(82, 0, 73, 0.1);
      padding-left: 20px;
    }

    .side-nav-item a:hover::before {
      transform: scaleY(1);
    }

    .side-nav-item.active a {
      background: rgba(82, 0, 73, 0.1);
      font-weight: 600;
    }

    .side-nav-item.active a::before {
      transform: scaleY(1);
    }

    /* 阅读进度条样式 */
    .progress-container {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: transparent;
      z-index: 1001;
    }

    .progress-bar {
      height: 100%;
      background: var(--primary-color);
      width: 0%;
      transition: width 0.1s ease;
      box-shadow: 0 0 10px rgba(82, 0, 73, 0.3);
    }

    /* 参考文献样式优化 - 使用更精确的选择器 */
    div.content-section h2[id="references"] + a[id^="ref"],
    div.content-section a[id^="ref"] + a[id^="ref"] {
      display: block;
      margin-top: 20px;
      padding-bottom: 10px;
      border-bottom: 1px solid rgba(82, 0, 73, 0.1);
    }
    
    div.content-section a[id^="ref"]:nth-of-type(odd) {
      background-color: rgba(245, 245, 245, 0.5);
      padding: 10px;
      border-radius: var(--border-radius);
    }
    
    /* 强制样式应用 */
    div.content-section a[id^="ref"] {
      display: block !important;
      margin-top: 15px !important;
    }
    
    /* 调整Similar compound表格列宽 */
    .table th:nth-child(1), 
    .table td:nth-child(1) {
      width: 12%;
    }
    
    .table th:nth-child(2), 
    .table td:nth-child(2) {
      width: 12%;
    }
    
    .table th:nth-child(3), 
    .table td:nth-child(3) {
      width: 10%;
    }
    
    .table th:nth-child(4), 
    .table td:nth-child(4) {
      width: 12%;
    }
    
    .table th:nth-child(5), 
    .table td:nth-child(5) {
      width: 54%;
    }
    
    /* 确保Structure列的图片适当显示 */
    .table td:nth-child(5) img {
      max-width: 100%;
      height: auto;
    }
  </style>
</head>
<body>
  <!-- 阅读进度条 -->
  <div class="progress-container">
    <div class="progress-bar" id="progressBar"></div>
  </div>

  <!-- 导航球 -->
  <div class="nav-ball" id="navBall">
    <div class="nav-ball-icon">
      <span></span>
      <span></span>
      <span></span>
    </div>
  </div>

  <!-- 遮罩层 -->
  <div class="overlay" id="overlay"></div>

  <!-- 侧边导航 -->
  <div class="side-nav" id="sideNav">
    <ul>
      <li class="side-nav-item"><a href="#timeline">Timeline</a></li>
      <li class="side-nav-item"><a href="#description">Description</a></li>
      <li class="side-nav-item"><a href="#SELEX">SELEX</a></li>
      <li class="side-nav-item"><a href="#Structure">Structure</a></li>
      <li class="side-nav-item"><a href="#ligand-recognition">Ligand information</a></li>
      <li class="side-nav-item"><a href="#references">References</a></li>
    </ul>
  </div>

  <script>
    // 导航球切换
    const navBall = document.getElementById('navBall');
    const sideNav = document.getElementById('sideNav');
    const overlay = document.getElementById('overlay');

    navBall.addEventListener('click', () => {
      navBall.classList.toggle('active');
      sideNav.classList.toggle('active');
      overlay.classList.toggle('active');
    });

    overlay.addEventListener('click', () => {
      navBall.classList.remove('active');
      sideNav.classList.remove('active');
      overlay.classList.remove('active');
    });

    // 阅读进度条
    window.addEventListener('scroll', () => {
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      document.getElementById('progressBar').style.width = scrolled + '%';
    });

    // 平滑滚动和导航项激活
    const sections = document.querySelectorAll('h2[id]');
    const navItems = document.querySelectorAll('.side-nav-item a');

    window.addEventListener('scroll', () => {
      let current = '';
      sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= sectionTop - 200) {
          current = section.getAttribute('id');
        }
      });

      navItems.forEach(item => {
        item.parentElement.classList.remove('active');
        if (item.getAttribute('href').slice(1) === current) {
          item.parentElement.classList.add('active');
        }
      });
    });

    document.querySelectorAll('.side-nav a').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
          targetElement.scrollIntoView({
            behavior: 'smooth'
          });
          // 关闭导航菜单
          navBall.classList.remove('active');
          sideNav.classList.remove('active');
          overlay.classList.remove('active');
        }
      });
    });

    // Timeline动画效果
    const observerOptions = {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.animationPlayState = 'running';
        }
      });
    }, observerOptions);

    // 观察所有timeline条目
    document.querySelectorAll('.entry').forEach(entry => {
      entry.style.animationPlayState = 'paused';
      observer.observe(entry);
    });
  </script>

<div class="content-section">
  <h2 class="section-title" id="timeline">Timeline</h2>
<div class="timeline">
  <div class="entry">
    <div class="title">
      <h3><a href="https://pubmed.ncbi.nlm.nih.gov/7510417/" target="_blank" style="color:#520049">1994</a></h3>
    </div>
    <div class="body">
      <p>Aptamers are isolated out for the first time<sup>[<a href="#ref1" style="color:#520049">1</a>]</sup></p>
    </div>
  </div>
  <div class="entry">
    <div class="title">
      <h3><a href="https://pubmed.ncbi.nlm.nih.gov/9224568/" target="_blank" style="color:#520049">1997</a></h3>
    </div>
    <div class="body">
      <p>First demonstrated that the aptamer could be linked to stem II of a self-cleaving hammerhead ribozyme<sup>[<a href="#ref2" style="color:#520049">2</a>]</sup></p>
    </div>
  </div>
  <div class="entry">
    <div class="title">
      <h3><a href="https://pubmed.ncbi.nlm.nih.gov/9253414/" target="_blank" style="color:#520049">1997</a></h3>
    </div>
    <div class="body">
      <p>Determination of RNA structural interactions in the theophylline ligand binding site using NMR techniques<sup>[<a href="#ref3" style="color:#520049">3</a>]</sup></p>
    </div>
  </div>
    <div class="entry">
    <div class="title">
      <h3><a href="https://pubmed.ncbi.nlm.nih.gov/10097080/" target="_blank" style="color:#520049">1999</a></h3>
    </div>
    <div class="body">
      <p>First discovery of theophylline-reactive riboswitches for controlling gene expression in vivo<sup>[<a href="#ref4" style="color:#520049">4</a>]</sup></p>
    </div>
  </div>
  <div class="entry">
    <div class="title">
      <h3><a href="https://pubmed.ncbi.nlm.nih.gov/11266567/" target="_blank" style="color:#520049">2001</a></h3>
    </div>
    <div class="body">
      <p>Created a binary RNA switch by linking the theophylline and FMN aptamers to the hammerhead<sup>[<a href="#ref5" style="color:#520049">5</a>]</sup></p>
    </div>
  </div>
  <div class="entry">
    <div class="title">
      <h3><a href="https://pubmed.ncbi.nlm.nih.gov/15826145/" target="_blank" style="color:#520049">2005</a></h3>
    </div>
    <div class="body">
      <p>Demonstrated that the aptamer can be truncated to a 13-mer aptamer and still retain selective binding<sup>[<a href="#ref6" style="color:#520049">6</a>]</sup></p>
    </div>
  </div>
  <div class="entry">
    <div class="title">
      <h3><a href="https://pubmed.ncbi.nlm.nih.gov/15723047/" target="_blank" style="color:#520049">2005</a></h3>
    </div>
    <div class="body">
      <p>Theophylline-controlled 'anti-switch' found to control green fluorescent protein expression in Saccharomyces cerevisiae<sup>[<a href="#ref7" style="color:#520049">7</a>]</sup></p>
    </div>
  </div>
  <div class="entry">
    <div class="title">
      <h3><a href="https://pubmed.ncbi.nlm.nih.gov/16513347/" target="_blank" style="color:#520049">2006</a></h3>
    </div>
    <div class="body">
      <p>Young and Deiters added a second level of control by photocaging the theophylline ligand, resulting in a photochemical activation of the ribozyme by liberation of the caging group<sup>[<a href="#ref8" style="color:#520049">8</a>]</sup></p>
    </div>
  </div>
<div class="entry">
    <div class="title">
      <h3><a href="https://pubmed.ncbi.nlm.nih.gov/16996258/" target="_blank" style="color:#520049">2007</a></h3>
    </div>
    <div class="body">
      <p>Developed a computational model to generate functional theophylline ribozymes<sup>[<a href="#ref9" style="color:#520049">9</a>]</sup></p>
    </div>
  </div>
  <div class="entry">
    <div class="title">
      <h3><a href="https://pubmed.ncbi.nlm.nih.gov/19033367/" target="_blank" style="color:#520049">2009</a></h3>
    </div>
    <div class="body">
      <p>A flow cytometry-based screen for identifying synthetic riboswitches that induce robust increases in gene expression in the presence of theophylline<sup>[<a href="#ref10" style="color:#520049">10</a>]</sup></p>
    </div>
  </div>
  <div class="entry">
    <div class="title">
      <h3><a href="https://pubmed.ncbi.nlm.nih.gov/23452219/" target="_blank" style="color:#520049">2013</a></h3>
    </div>
    <div class="body">
      <p>Using a computational model, Penchovsky developed and tested a theophyllinehammerhead ribozyme fusion that was inactivated with a 30-fold dynamic range<sup>[<a href="#ref11" style="color:#520049">11</a>]</sup></p>
    </div>
  </div>
   <div class="entry">
    <div class="title">
      <h3><a href="https://pubmed.ncbi.nlm.nih.gov/23654267/" target="_blank" style="color:#520049">2013</a></h3>
    </div>
    <div class="body">
      <p>Developed three OFF theophylline switches that are functional in vivo <sup>[<a href="#ref12" style="color:#520049">12</a>]</sup></p>
    </div>
  </div>
   <div class="entry">
    <div class="title">
      <h3><a href="https://pubmed.ncbi.nlm.nih.gov/25726466/" target="_blank" style="color:#520049">2015</a></h3>
    </div>
    <div class="body">
      <p>The aptamers found to optimise ribose enlightenment<sup>[<a href="#ref13" style="color:#520049">13</a>]</sup></p>
    </div>
  </div>
   <div class="entry">
    <div class="title">
      <h3><a href="https://pubmed.ncbi.nlm.nih.gov/26594238/" target="_blank" style="color:#520049">2015</a></h3>
    </div>
    <div class="body">
      <p>The better standardization of gene expression or cellular processes<sup>[<a href="#ref14" style="color:#520049">14</a>]</sup></p>
    </div>
  </div>
   <div class="entry">
    <div class="title">
      <h3><a href="https://pubmed.ncbi.nlm.nih.gov/26642994/" target="_blank" style="color:#520049">2015</a></h3>
    </div>
    <div class="body">
      <p>Six new theophylline aptamers discovered using computerised screening<sup>[<a href="#ref15" style="color:#520049">15</a>]</sup></p>
    </div>
  </div>
   <div class="entry">
    <div class="title">
      <h3><a href="https://pubmed.ncbi.nlm.nih.gov/29319503/" target="_blank" style="color:#520049">2018</a></h3>
    </div>
    <div class="body">
      <p>The aptamers can build logic gates in cells<sup>[<a href="#ref16" style="color:#520049">16</a>]</sup></p>
    </div>
  </div>
   <div class="entry">
    <div class="title">
      <h3><a href="https://pubmed.ncbi.nlm.nih.gov/30119599/" target="_blank" style="color:#520049">2018</a></h3>
    </div>
    <div class="body">
      <p>New theophylline-reactive aptamers are screened from a synthetic library in Escherichia coli<sup>[<a href="#ref17" style="color:#520049">17</a>]</sup></p>
    </div>
  </div>
  <div class="entry">
    <div class="title">
      <h3><a href="https://pubmed.ncbi.nlm.nih.gov/36413497/" target="_blank" style="color:#520049">2022</a></h3>
    </div>
    <div class="body">
      <p>The structure of the aptamer, both in isolation and in complex with theophylline and the four best hits, was determined by X-ray crystallography<sup>[<a href="#ref30" style="color:#520049">30</a>]</sup></p>
      </div>
    </div>
  </div>
</div>

<div class="content-section">
  <h2 class="section-title" id="description">Description</h2>
<p>In <span class="highlight-text">1994</span>, Polisky, B. et al. used <span class="highlight-text">SELEX</span> to screen for high-affinity RNA aptamers with theophylline-binding solution structures. In <span class="highlight-text">1997</span>, <span class="highlight-text">NMR techniques</span> visualised the interaction of RNA structures in the ligand-binding site. In <span class="highlight-text">1998</span>, it was found that <span class="highlight-text">U27 and G27 RNAs</span> bound theophylline with low-affinity (Kd values > 4 μM). NMR spectroscopy of U27 RNA revealed an <span class="highlight-text">A7-U27 base pair</span> in the free RNA, which prevented the formation of a key structural motif in the critical base platform and thus inhibited theophylline binding. In <span class="highlight-text">2022</span>, the crystal structure of the theophylline aptamer was resolved<sup>[<a href="#ref1" style="color:#520049">1</a></sup><sup>,<a href="#ref3" style="color:#520049">3</a></sup><sup>,<a href="#ref4" style="color:#520049">4</a></sup><sup>,<a href="#ref30" style="color:#520049">30</a></sup><sup>]</sup>.</p>
</div>

<div class="content-section">
  <h2 class="section-title" id="SELEX">SELEX</h2>
<p>In <span class="highlight-text">1994</span>, Polisky, B et al. used <span class="highlight-text">SELEX</span> to identify RNA molecules with an affinity for theophylline. They created a pool of <span class="highlight-text">10<sup>14</sup> RNA molecules</span>, each comprising a <span class="highlight-text">40-nucleotide region</span> of random sequence. The RNA pool was then introduced to a <span class="highlight-text">Sepharose column</span> that had <span class="highlight-text">1-carboxypropyl theophylline</span> covalently cross-linked to it. The bound RNA was subsequently eluted by adding <span class="highlight-text">0.1 M theophylline</span>. The eluted RNA was then converted to DNA and amplified via <span class="highlight-text">polymerase chain reaction (PCR)</span>, following the described procedure<sup>[<a href="#ref1" style="color:#520049">1</a>]</sup>.</p>
<p>Detailed information are accessible on <a href="{{ site.url }}{{ site.baseurl }}/SELEX" target="_blank" style="color:#520049"><b><i>SELEX</i></b></a> page.</p>
</div>

<div class="content-section">
  <h2 class="section-title" id="Structure">Structure</h2>
<div class="blowheader_box">2D representation</div>
<p>In 1997, Pardi.A. et al. obtained multiple different RNA sequences through in vitro selection procedures, including the SELEX technique, and designed a high-affinity RNA aptamer after comparing the information of these sequences. The RNA aptamer is characterised by a sequence that forms a distinct secondary structure, as illustrated in the subsequent diagrams. Here we used RiboDraw to complete the figure, based the 3D structure information<sup>[<a href="#ref3" style="color:#520049">3</a>]</sup>.</p>
<div class="sequence">5'-GGCAUACCAGCCGAAAGGCCCUUGGCAGCGUC-3'</div>
<img src="/images/2D/Theophylline_aptamer_2D.svg" alt="drawing" style="width:800px;height:350px;display:block;margin:0 auto;border-radius:0;" class="img-responsive">

<div class="blowheader_box">3D visualisation</div>             
<p>In 1997, Pardi.A. et al. used NMR and X-PLOR 3.113 calculations to demonstrate the solution structure of a high-affinity RNA-theophylline complex, where the <span class="highlight-text">C27 nucleotide</span> was identified as the key residue for recognising theophylline and discriminating it from caffeine. The PDB ID for the NMR structure of the RNA-theophylline complex is <span class="highlight-text">1EHT</span>. In 2022, Rogers.J. et al. determined the crystal structure of an RNA aptamer-theophylline complex. Owing to the high similarity between the solved NMR 3D structure and the following crystal 3D structure, only the crystal 3D structure is presented here. The PDB ID for the crystal structure of the theophylline aptamer is <span class="highlight-text">8D28</span><sup>[<a href="#ref3" style="color:#520049">3</a></sup><sup>,<a href="#ref30" style="color:#520049">30</a></sup><sup>]</sup>.</p>
<p>Additional available structures that have been solved and detailed information are accessible on <a href="{{ site.url }}{{ site.baseurl }}/structures" target="_blank" style="color:#520049"><b><i>Structures</i></b></a> page.</p>
<div><p style="text-align:right;margin-bottom: 0px;">(Clicking the "Settings/Controls info" to turn Spin off)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
  <table class="structure-table" style="table-layout:fixed;width:1000px;margin-left:auto;margin-right:auto;"><tr>
  <td style="text-align:center;padding-bottom: 0px;padding-left: 0px;padding-top: 0px;padding-right: 0px">
  <img src="/images/3D/Theophylline_aptamer_3D1.svg" alt="drawing" style="width:500px;margin-top: 0px;margin-bottom: 0px;" >
  </td>
  <td style="text-align:center;padding-bottom: 0px;padding-left: 0px;padding-top: 0px;padding-right: 0px">
  <html lang="en">
    <head>
      <meta charset="utf-8" />
      <meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <title>PDBe Molstar</title>
      <!-- Molstar CSS & JS -->
      <link rel="stylesheet" type="text/css" href="https://www.ebi.ac.uk/pdbe/pdb-component-library/css/pdbe-molstar-1.2.1.css">
      <script src="/js/mol/pdbe-molstar-plugin.js"></script>
        <style>
          * {
              margin: 0;
              padding: 0;
              box-sizing: border-box;
          }
          .msp-plugin ::-webkit-scrollbar-thumb {
              background-color: #474748  !important;
          }
          .msp-plugin .msp-layout-standard {
              border: 1px solid #efefef;
          }
          .viewerSection1 {
            padding-top: 0px;
          }
          .controlsSection1 {
            width: 300px;
              display: flex;
              float:left;
              padding: 0px 0 0 0;
              height:25px;
            }
            .controlBox1 {
              border: 0px solid lightgray;
              padding: 0px;
              margin-bottom: 0px;
            }
          #myViewer1{
            float:left;
            width:500px !important;
            height: 500px !important;
            position:relative;
            min-width: 500px;
            min-height: 500px;
          }
          
          /* 确保Molstar插件不受外部样式影响 */
          .msp-plugin {
            width: 500px !important;
            height: 500px !important;
          }
        </style>
    </head>
    <body onload="customize()">
        <div class="controlsSection1">
            <button onclick="
              var selectSections1 = [
             {
  struct_asym_id: 'A',    
  start_residue_number:1, 
  end_residue_number:5, 
  color:{r:184,g:51,b:50}
},
{
  struct_asym_id: 'A', 
  start_residue_number:6, 
  end_residue_number:8, 
  color:{r:46,g:161,b:3}
},
{
  struct_asym_id: 'A', 
  start_residue_number:9, 
  end_residue_number:21, 
  color:{r:184,g:51,b:50}
},
{
  struct_asym_id: 'A', 
  start_residue_number:22, 
  end_residue_number:22, 
  color:{r:241,g:125,b:7}
},
{
  struct_asym_id: 'A', 
  start_residue_number:23, 
  end_residue_number:23, 
  color:{r:46,g:161,b:3}
},
{
  struct_asym_id: 'A', 
  start_residue_number:24, 
  end_residue_number:24, 
  color:{r:241,g:125,b:7}
},
{
   struct_asym_id: 'A', 
  start_residue_number:25, 
  end_residue_number:25, 
  color:{r:194,g:182,b:23}
},
{
  struct_asym_id: 'A', 
  start_residue_number:26, 
  end_residue_number:26, 
  color:{r:46,g:161,b:3}
},
{
   struct_asym_id: 'A', 
  start_residue_number:27, 
  end_residue_number:27, 
  color:{r:194,g:182,b:23}
},
{
  struct_asym_id: 'A',    
  start_residue_number:28, 
  end_residue_number:28, 
  color:{r:46,g:161,b:3}
},
{
  struct_asym_id: 'A',    
  start_residue_number:29, 
  end_residue_number:33, 
  color:{r:184,g:51,b:50}
},
{
  struct_asym_id: 'B',    
  start_residue_number:101, 
  end_residue_number:101, 
  color:{r:255,g:0,b:255}
}
              ]
            viewerInstance1.visual.select({ data: selectSections1, nonSelectedColor: {r:255,g:255,b:255}})" style="float:right;height:25px;width: 120px;">Color Selection</button><br><br>
          <button button style="float: left;height:25px;width: 120px;" onclick="viewerInstance1.visual.clearSelection()">Clear Selection</button><br><br>
      </div>
    <div class="viewerSection1">
    <!-- Molstar container -->
      <div id="myViewer1"></div>
    </div>
    <script>
      var viewerInstance1 = new PDBeMolstarPlugin();
      var options1 = {
        customData:{
        url:'/pdbfiles/WJL-8d28.pdb',
        format: 'pdb'},
        expanded: false,
        hideControls: true,
        bgColor: {r:255, g:255, b:255},
        }
      var viewerContainer1 = document.getElementById('myViewer1');
      viewerInstance1.render(viewerContainer1, options1);
  window.addEventListener('load', function() {
    var colorSelectionButton1 = document.querySelector('.controlsSection1 button');
    colorSelectionButton1.click();
  });
</script>
</body>
</html>
</td>
</tr>
</table>
</div>

<div class="blowheader_box">Binding pocket</div>             
<p>Left: Surface representation of the binding pocket of the aptamer generated from PDB ID: <span class="highlight-text">8D28</span> by X-ray Crystallography. <span class="highlight-text">Theophylline</span> (shown in sticks) is labeled in magenta. Right: The hydrogen bonds of binding sites of the aptamer bound with Theophylline.</p>
  <table class="binding-pocket-table" style="table-layout:fixed;width:1000px;margin-left:auto;margin-right:auto;"><tr>
  <td style="text-align:center;padding-bottom: 0px;padding-left: 0px;padding-top: 0px;padding-right: 0px">
  <img src="/images/Binding_pocket/Theophylline_aptamer_binding_pocket1.svg" alt="drawing" style="width:500px;margin-top: 0px;margin-bottom: 0px;" >
  </td>
  <td style="text-align:center;padding-bottom: 0px;padding-right: 0px;padding-top: 0px;padding-right: 0px">
  <img src="/images/Binding_pocket/Theophylline_aptamer_binding_pocket2.svg" alt="drawing" style="width:500px;margin-top: 0px;margin-bottom: 0px;" >
  </td>
  </tr>
  </table>
  <br>
  <br>
</div>

<div class="content-section">
  <h2 class="section-title" id="ligand-recognition">Ligand information</h2>
  
  <div class="blowheader_box">SELEX ligand</div>
  <p>To determine the dissociation constants (Kd) of the theophylline aptamer and its ligands, the RNA was synthesised with a <span class="highlight-text">Cy5 fluorophore</span> at the 3' end. Strand invasion assays were conducted by incubating the labelled aptamer with a complementary oligonucleotide carrying a fluorescence quencher. The fluorescence changes were measured upon the addition of various compounds, and the data were fitted to determine the <span class="highlight-text">IC50 values</span>, which served as an estimate of Kd. <span class="highlight-text">Surface plasmon resonance (SPR)</span> was used for precise Kd determination, where the RNA aptamer was immobilised on a CM5 sensor chip via biotin and NeutrAvidin. The ligands were injected at varying concentrations, and the binding data were analysed to obtain Kd values. The compounds <span class="highlight-text">TAL1, TAL2, TAL3, and TAL4</span> were found to have Kd values of <span class="highlight-text">0.0020, 0.0091, 0.023, and 0.28 µM</span>, respectively, demonstrating higher affinity than theophylline (0.67 µM). Theophylline aptamer ligand 1 (TAL1), is an aminomethyl-substituted pteridinone that has a similar molecular weight as that of theophylline. The other three (TAL2, TAL3, and TAL4) have higher molecular weights, with differing substitutions of a common quinazolinone ring system<sup>[<a href="#ref30">30</a>]</sup>.</p>
  
  <img src="/images/SELEX_ligand/Theophylline_SELEX_ligand.svg" alt="SELEX ligands" class="img-responsive">

  <div class="blowheader_box">Structure ligand</div>
  <p>A methylxanthine derivative from tea with diuretic, smooth muscle relaxant, bronchial dilation, cardiac and central nervous system stimulant activities. Mechanistically, theophylline acts as a <span class="highlight-text">phosphodiesterase inhibitor</span>, <span class="highlight-text">adenosine receptor blocker</span>, and <span class="highlight-text">histone deacetylase activator</span>. Theophylline is marketed under several brand names such as <span class="highlight-text">Uniphyl and Theochron</span>, and it is indicated mainly for <span class="highlight-text">asthma, bronchospasm, and COPD</span>.-----From<a href="https://go.drugbank.com/drugs/DB00277" target="_blank"><b>Drugbank</b></a></p>

  <div class="info-box">
    <p><b>PubChem CID:</b> a unique identifier for substances in the <a href="https://pubchem.ncbi.nlm.nih.gov/" target="_blank"><b>PubChem database</b></a>.</p>
    <p><b><a href="https://commonchemistry.cas.org/" target="_blank"><b>CAS</b></a> number:</b> a global registry number for chemical substances.</p>
    <p><b><a href="https://go.drugbank.com/" target="_blank"><b>Drugbank</b></a>:</b> a comprehensive database with detailed information on drugs and drug targets.</p>
  </div>

  <table class="table">
  <thead>
      <tr>
        <th>Name</th>
        <th>PubChem CID</th>
        <th>Molecular Formula</th>
        <th>Molecular Weight</th>
        <th>CAS</th>
        <th>Solubility</th>
        <th>Drugbank ID</th>
      </tr>
  </thead>
    <tbody>
      <tr>
        <td>Theophylline</td>
        <td><a href="https://pubchem.ncbi.nlm.nih.gov/compound/2153" target="_blank">2153</a></td>
        <td>C<sub>7</sub>H<sub>8</sub>N<sub>4</sub>O<sub>2</sub></td>
        <td>180.16 g/mol</td>
        <td><a href="https://commonchemistry.cas.org/detail?cas_rn=58-55-9" target="_blank">58-55-9</a></td>
        <td>7360mg/L (at 25 °C)</td>
        <td><a href="https://go.drugbank.com/drugs/DB00277" target="_blank">DB00277</a></td>
      </tr>
	  </tbody>
  </table>

  <div class="structure-images">
    <img src="/images/Structure_ligand/Theophylline_stru_ligand1.svg" alt="Structure ligand 1" class="img-responsive">
    <img src="/images/Structure_ligand/Theophylline_stru_ligand2.svg" alt="Structure ligand 2" class="img-responsive">
  </div>

  <div class="blowheader_box">Similar compound(s)</div>
  <p>We screened the compounds with great similarity to theophylline by using the <a href="https://zinc15.docking.org/" target="_blank"><b>ZINC database</b></a> and showed some of the compounds' structure diagrams. For some CAS numbers not available, we will supplement them with <span class="highlight-text">Pubchem CID</span>.</p>

  <div class="info-box">
    <p><b>ZINC ID:</b> a compound identifier used by the <a href="https://zinc15.docking.org/" target="_blank"><b>ZINC database</b></a>, one of the largest repositories for virtual screening of drug-like molecules.</p>
    <p><b>PubChem CID:</b> a unique identifier for substances in the <a href="https://pubchem.ncbi.nlm.nih.gov/" target="_blank"><b>PubChem database</b></a>.</p>
    <p><b><a href="https://commonchemistry.cas.org/" target="_blank"><b>CAS</b></a> number:</b> a global registry number for chemical substances.</p>
  </div>

  <table class="table">
  <thead>
      <tr>
        <th>ZINC ID</th>
        <th>Name</th>
        <th>CAS</th>
        <th>Pubchem CID</th>
        <th>Structure</th>
      </tr>
  </thead>
    <tbody>
      <tr>
        <td><a href="https://zinc15.docking.org/substances/ZINC18043251/" target="_blank">ZINC18043251</a></td>
        <td>Theophylline</td>
        <td><a href="https://commonchemistry.cas.org/detail?cas_rn=58-55-9" target="_blank">58-55-9</a></td>
        <td><a href="https://pubchem.ncbi.nlm.nih.gov/compound/2153" target="_blank">2153</a></td>
        <td><img src="/images/Similar_compound/Theophylline_Simi_compound1.svg" alt="drawing" style="width:500px"  px="" /></td>
      </tr>
      <tr>
        <td><a href="https://zinc15.docking.org/substances/ZINC13517144/" target="_blank">ZINC13517144</a></td>
        <td>1-Methylxanthine</td>
        <td><a href="https://commonchemistry.cas.org/detail?cas_rn=6136-37-4" target="_blank">6136-37-4</a></td>
        <td><a href="https://pubchem.ncbi.nlm.nih.gov/compound/80220" target="_blank">80220</a></td>
        <td><img src="/images/Similar_compound/Theophylline_Simi_compound2.svg" alt="drawing" style="width:500px"  px="" /></td>
      </tr>
      <tr>
        <td><a href="https://zinc15.docking.org/substances/ZINC4685854/" target="_blank">ZINC4685854</a></td>
        <td>3-Methylxanthine</td>
        <td><a href="https://commonchemistry.cas.org/detail?cas_rn=1076-22-8" target="_blank">1076-22-8</a></td>
        <td><a href="https://pubchem.ncbi.nlm.nih.gov/compound/70639" target="_blank">70639</a></td>
        <td><img src="/images/Similar_compound/Theophylline_Simi_compound3.svg" alt="drawing" style="width:500px"  px="" /></td>
      </tr>
      <tr>
        <td><a href="https://zinc15.docking.org/substances/ZINC100018165/" target="_blank">ZINC100018165</a></td>
        <td>8-Chlorotheophylline</td>
        <td><a href="https://commonchemistry.cas.org/detail?cas_rn=85-18-7" target="_blank">85-18-7</a></td>
        <td><a href="https://pubchem.ncbi.nlm.nih.gov/compound/10661" target="_blank">10661</a></td>
        <td><img src="/images/Similar_compound/Theophylline_Simi_compound4.svg" alt="drawing" style="width:500px"  px="" /></td>
      </tr>
      <tr>
        <td><a href="https://zinc15.docking.org/substances/ZINC100005670/" target="_blank">ZINC100005670</a></td>
        <td>8-Bromotheophylline</td>
        <td><a href="https://commonchemistry.cas.org/detail?cas_rn=10381-75-6" target="_blank">10381-75-6</a></td>
        <td><a href="https://pubchem.ncbi.nlm.nih.gov/compound/11808" target="_blank">11808</a></td>
        <td><img src="/images/Similar_compound/Theophylline_Simi_compound5.svg" alt="drawing" style="width:500px"  px="" /></td>
      </tr>
      <tr>
        <td><a href="https://zinc15.docking.org/substances/ZINC1084/" target="_blank">ZINC1084</a></td>
        <td>caffeine</td>
        <td><a href="https://commonchemistry.cas.org/detail?cas_rn=21399" target="_blank">21399</a></td>
        <td><a href="https://pubchem.ncbi.nlm.nih.gov/compound/2519" target="_blank">2519</a></td>
        <td><img src="/images/Similar_compound/Theophylline_Simi_compound6.svg" alt="drawing" style="width:500px"  px="" /></td>
      </tr>
      <tr>
        <td><a href="https://zinc15.docking.org/substances/ZINC8616085/" target="_blank">ZINC8616085</a></td>
        <td>3-Methylguanine</td>
        <td><a href="https://commonchemistry.cas.org/detail?cas_rn=2958-98-7" target="_blank">2958-98-7</a></td>
        <td><a href="https://pubchem.ncbi.nlm.nih.gov/compound/76292" target="_blank">76292</a></td>
        <td><img src="/images/Similar_compound/Theophylline_Simi_compound7.svg" alt="drawing" style="width:500px"  px="" /></td>
      </tr>
      <tr>
        <td><a href="https://zinc15.docking.org/substances/ZINC100043983/" target="_blank">ZINC100043983</a></td>
        <td>1,3-Dimethyluric acid</td>
        <td><a href="https://commonchemistry.cas.org/detail?cas_rn=944-73-0" target="_blank">944-73-0</a></td>
        <td><a href="https://pubchem.ncbi.nlm.nih.gov/compound/70346" target="_blank">70346</a></td>
        <td><img src="/images/Similar_compound/Theophylline_Simi_compound8.svg" alt="drawing" style="width:500px"  px="" /></td>
      </tr>
      <tr>
        <td><a href="https://zinc15.docking.org/substances/ZINC403604/" target="_blank">ZINC403604</a></td>
        <td>Isocaffeine</td>
        <td><a href="https://commonchemistry.cas.org/detail?cas_rn=519-32-4" target="_blank">519-32-4</a></td>
        <td><a href="https://pubchem.ncbi.nlm.nih.gov/compound/1326" target="_blank">1326</a></td>
        <td><img src="/images/Similar_compound/Theophylline_Simi_compound9.svg" alt="drawing" style="width:500px"  px="" /></td>
      </tr>
	  </tbody>
  </table>
</div>

<div class="content-section">
  <h2 class="section-title" id="references">References</h2>
                
<a id="ref1"></a><font><strong>[1] High-resolution molecular discrimination by RNA.</strong></font><br />
Jenison, R. D., Gill, S. C., Pardi, A., & Polisky, B.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/7510417/" target="_blank" style="color:#520049" >Science (New York, N.Y.), 263(5152), 1425–1429. (1994)</a>
<br />
                
<a id="ref2"></a><font><strong>[2] Rational design of allosteric ribozymes.</strong></font><br />
Tang, J., & Breaker, R. R.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/9224568/" target="_blank" style="color:#520049">Chemistry & biology, 4(6), 453–459. (1997)</a>
<br />
                
<a id="ref3"></a><font><strong>[3] Interlocking structural motifs mediate molecular discrimination by a theophylline-binding RNA.</strong></font><br />
Zimmermann, G. R., Jenison, R. D., Wick, C. L., Simorre, J. P., & Pardi, A.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/9253414/" target="_blank" style="color:#520049"> Nature structural biology, 4(8), 644–649. (1997)</a>
<br />
                
<a id="ref4"></a><font><strong>[4] A semiconserved residue inhibits complex formation by stabilizing interactions in the free state of a theophylline-binding RNA.</strong></font><br />
Zimmermann, G. R., Shields, T. P., Jenison, R. D., Wick, C. L., & Pardi, A.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/9636066/" target="_blank" style="color:#520049">Biochemistry, 37(25), 9186–919. (1998)</a>
<br />
                
<a id="ref5"></a><font><strong>[5] Engineering precision RNA molecular switches.</strong></font><br />
Soukup, G. A., & Breaker, R. R.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/10097080/" target="_blank" style="color:#520049">Proceedings of the National Academy of Sciences of the United States of America, 96(7), 3584–3589. (1999)</a>
<br />
                
<a id="ref6"></a><font><strong>[6] Design of allosteric hammerhead ribozymes activated by ligand-induced structure stabilization.</strong></font><br />
Soukup, G. A., & Breaker, R. R.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/10425680/" target="_blank" style="color:#520049">Structure (London, England : 1993), 7(7), 783–791. (1999)</a>
<br />
                
<a id="ref7"></a><font><strong>[7] Molecular interactions and metal binding in the theophylline-binding core of an RNA aptamer.</strong></font><br />
Zimmermann, G. R., Wick, C. L., Shields, T. P., Jenison, R. D., & Pardi, A.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/10836787/" target="_blank" style="color:#520049">RNA (New York, N.Y.), 6(5), 659–667. (2000)</a>
<br />
                
<a id="ref8"></a><font><strong>[8] Cooperative binding of effectors by an allosteric ribozyme.</strong></font><br />
Jose, A. M., Soukup, G. A., & Breaker, R. R.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/11266567/" target="_blank" style="color:#520049">Nucleic acids research, 29(7), 1631–1637. (2001)</a>
<br />
                
<a id="ref9"></a><font><strong>[9] Unnatural base pairs mediate the site-specific incorporation of an unnatural hydrophobic component into RNA transcripts.</strong></font><br />
Endo, M., Mitsui, T., Okuni, T., Kimoto, M., Hirao, I., & Yokoyama, S.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/15109659/" target="_blank" style="color:#520049">Bioorganic & medicinal chemistry letters, 14(10), 2593–2596. (2004)</a>
<br />
                
<a id="ref10"></a><font><strong>[10]  A theophylline responsive riboswitch based on helix slipping controls gene expression in vivo.</strong></font><br />
Suess, B., Fink, B., Berens, C., Stentz, R., & Hillen, W.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/15004248/" target="_blank" style="color:#520049"> Nucleic acids research, 32(4), 1610–1614. (2004)</a>
<br />
                
<a id="ref11"></a><font><strong>[11] Unusually short RNA sequences: design of a 13-mer RNA that selectively binds and recognizes theophylline.</strong></font><br />
Anderson, P. C., & Mecozzi, S.<br />
  <a href="https://pubmed.ncbi.nlm.nih.gov/15826145/" target="_blank" style="color:#520049" >Journal of the American Chemical Society, 127(15), 5290–5291. (2005)</a>
<br />

<a id="ref12"></a><font><strong>[12] Programmable ligand-controlled riboregulators of eukaryotic gene expression.</strong></font><br />
Bayer, T. S., & Smolke, C. D.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/15723047/" target="_blank" style="color:#520049" >Nature biotechnology, 23(3), 337–343. (2005)</a>
<br />

<a id="ref13"></a><font><strong>[13] Photochemical hammerhead ribozyme activation.</strong></font><br />
Young, D. D., & Deiters, A.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/16513347/" target="_blank" style="color:#520049" >Bioorganic & medicinal chemistry letters, 16(10), 2658–2661. (2006)</a>
<br />

<a id="ref14"></a><font><strong>[14] Computational selection of nucleic acid biosensors via a slip structure model.</strong></font><br />
Hall, B., Hesselberth, J. R., & Ellington, A. D.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/16996258/" target="_blank" style="color:#520049" >Biosensors & bioelectronics, 22(9-10), 1939–1947. (2007)</a>
<br />

<a id="ref15"></a><font><strong>[15] A high-throughput screen for synthetic riboswitches reveals mechanistic insights into their function.</strong></font><br />
Lynch, S. A., Desai, S. K., Sajja, H. K., & Gallivan, J. P.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/17317571/" target="_blank" style="color:#520049" > Chemistry & biology, 14(2), 173–184. (2007)</a>
<br />

<a id="ref16"></a><font><strong>[16] A flow cytometry-based screen for synthetic riboswitches.</strong></font><br />
Lynch, S. A., & Gallivan, J. P.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/19033367/" target="_blank" style="color:#520049" >Nucleic acids research, 37(1), 184–192.  (2009)</a>
<br />

<a id="ref17"></a><font><strong>[17] Design principles for ligand-sensing, conformation-switching ribozymes.</strong></font><br />
Chen, X., & Ellington, A. D.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/20041206/" target="_blank" style="color:#520049" > PLoS computational biology, 5(12), e1000620. (2009)</a>
<br />

<a id="ref18"></a><font><strong>[18]  Kinetic analysis of aptazyme-regulated gene expression in a cell-free translation system: modeling of ligand-dependent and -independent expression.</strong></font><br />
Kobori, S., Ichihashi, N., Kazuta, Y., Matsuura, T., & Yomo, T.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/22733807/" target="_blank" style="color:#520049" >RNA (New York, N.Y.), 18(8), 1458–1465. (2012)</a>
<br />

<a id="ref19"></a><font><strong>[19] Computational design and biosensor applications of small molecule-sensing allosteric ribozymes.</strong></font><br />
Penchovsky R.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/23452219/" target="_blank" style="color:#520049" >Biomacromolecules, 14(4), 1240–1249. (2013)</a>
<br />

<a id="ref20"></a><font><strong>[20] Theophylline-dependent riboswitch as a novel genetic tool for strict regulation of protein expression in Cyanobacterium Synechococcus elongatus PCC 7942.</strong></font><br />
Nakahira, Y., Ogawa, A., Asano, H., Oyama, T., & Tozawa, Y.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/23969558/" target="_blank" style="color:#520049" > Plant & cell physiology, 54(10), 1724–1735. (2013)</a>
<br />

<a id="ref21"></a><font><strong>[21] Modularity of select riboswitch expression platforms enables facile engineering of novel genetic regulatory devices.</strong></font><br />
Ceres, P., Garst, A. D., Marcano-Velázquez, J. G., & Batey, R. T.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/23654267/" target="_blank" style="color:#520049" >ACS synthetic biology, 2(8), 463–472. (2013)</a>
<br />

<a id="ref22"></a><font><strong>[22] Thermodynamic and kinetic folding of riboswitches.</strong></font><br />
Badelt, S., Hammer, S., Flamm, C., & Hofacker, I. L.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/25726466/" target="_blank" style="color:#520049" > Methods in enzymology, 553, 193–213. (2015)</a>
<br />

<a id="ref23"></a><font><strong>[23] Engineering dynamic cell cycle control with synthetic small molecule-responsive RNA devices.</strong></font><br />
Wei, K. Y., & Smolke, C. D<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/26594238/" target="_blank" style="color:#520049" >Journal of biological engineering,  9, 21. (2015)</a>
<br />
                    
<a id="ref24"></a><font><strong>[24] Searching the Sequence Space for Potent Aptamers Using SELEX in Silico.</strong></font><br />
Zhou, Q., Xia, X., Luo, Z., Liang, H., & Shakhnovich, E.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/26642994/" target="_blank" style="color:#520049" >Journal of chemical theory and computation, 11(12), 5939–5946. (2015)</a>
<br />

<a id="ref25"></a><font><strong>[25] Ynthesizing artificial devices that redirect cellular information at will.</strong></font><br />
Liu, Y., Li, J., Chen, Z., Huang, W., & Cai, Z.<br />
  <a href="https://pubmed.ncbi.nlm.nih.gov/29319503/" target="_blank" style="color:#520049" >eLife, 7, e31936. (2018)</a>
<br />

<a id="ref26"></a><font><strong>[26] Engineering Riboswitches in Vivo Using Dual Genetic Selection and Fluorescence-Activated Cell Sorting.</strong></font><br />
Page, K., Shaffer, J., Lin, S., Zhang, M., & Liu, J. M.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/30119599/" target="_blank" style="color:#520049" > ACS synthetic biology, 7(9), 2000–2006. (2018)</a>
<br />

<a id="ref27"></a><font><strong>[27] Detection of Low-Abundance Metabolites in Live Cells Using an RNA Integrator.</strong></font><br />
You, M., Litke, J. L., Wu, R., & Jaffrey, S. R.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/30773480/" target="_blank" style="color:#520049" >Cell chemical biology, 26(4), 471–481.e3. (2019)</a>
<br />

<a id="ref28"></a><font><strong>[28] Controlling Heterogeneity and Increasing Titer from Riboswitch-Regulated Bacillus subtilis Spores for Time-Delayed Protein Expression Applications.</strong></font><br />
Tamiev, D., Lantz, A., Vezeau, G., Salis, H., & Reuel, N. F.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/31490060/" target="_blank" style="color:#520049" >ACS synthetic biology, 8(10), 2336–2346. (2019)</a>
<br />

<a id="ref29"></a><font><strong>[29] The Theophylline Aptamer: 25 Years as an Important Tool in Cellular Engineering Research.</strong></font><br />
Wrist, A., Sun, W., & Summers, R. M.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/32142605/" target="_blank" style="color:#520049" >ACS synthetic biology, 9(4), 682–697. (2020)</a>
<br />

<a id="ref30"></a><font><strong>[30] Discovery of small molecules that target a tertiary-structured RNA.</strong></font><br />
Menichelli, E., Lam, B. J., Wang, Y., Wang, V. S., Shaffer, J., Tjhung, K. F., Bursulaya, B., Nguyen, T. N., Vo, T., Alper, P. B., McAllister, C. S., Jones, D. H., Spraggon, G., Michellys, P. Y., Joslin, J., Joyce, G. F., & Rogers, J.<br />
  <a href="https://pubmed.ncbi.nlm.nih.gov/36413497/" target="_blank" style="color:#520049" >Proceedings of the National Academy of Sciences of the United States of America, 119(48), e2213117119. (2022)</a>
<br />
</div>
