---
layout: theophylline_style
title:  "3Dpol-aptamer"
date:   2024-05-17 00:00:00
author: Bichun Wu, Jiaxin Zhao
categories: Aptamer
---
<html>
<head>
  <style>
    /* 可以添加页面特定样式 */
  </style>
</head>
<body>
  <!-- 内容将按照Theophylline的样式格式进行调整 -->

  <div class="content-section">
    <h2 class="section-title" id="description">Description</h2>
    <p>In 2006, Ellingham, M., & Stonehouse, N. J.  report the selection and characterization of RNA aptamers to the 3D RdRp, a key part of the FMDV replication complex. This is the first report of aptamer selection to any protein of this economically important animal pathogen. They have characterized three aptamers (F38, F47, and F52) that inhibit the in vitro activity of the enzyme with IC50 values of 15.8 nM, 10.6 nM, and 16.4 nM, respectively. One aptamer retains this inhibitory ability when truncated to a 32mer (F47tr) with an IC50 of 10.2 nM<sup>[<a href="#ref2" style="color:#520049">2</a>]</sup>.</p>
  </div>

  <div class="content-section">
    <h2 class="section-title" id="SELEX">SELEX</h2>
    <p>In 2006, Ellingham, M., & Stonehouse, N. J. undertaken Fifteen rounds of selection using a degenerate library of ∼10<sup>15</sup> sequences, consisting of an N30 random region flanked by primer sequences for amplification and in vitro transcription.  As expected, the selected pool displayed increased affinity for 3Dpol compared with the naive RNA population as assessed by electrophoretic mobility shift assays . Fifty-two cDNA clones were prepared from the round 15 selected pool, of which 25 were selected at random for detailed analysis and sequencing . Selection resulted in some of the aptamers incorporating N30 regions smaller than the original 30 nucleotides. The greatest reductions were seen with aptamers F4, F6, F12, and F38<sup>[<a href="#ref2" style="color:#520049">2</a>]</sup>.</p>
    <p>Detailed information are accessible on <a href="{{ site.url }}{{ site.baseurl }}/SELEX" target="_blank" style="color:#520049"><b><i>SELEX</i></b></a> page.</p>
  </div>

  <div class="content-section">
    <h2 class="section-title" id="Structure">Structure</h2>
    <p>The 2D structure of the figures is based on the prediction results of the RNA fold website by ribodraw tool to draw<sup>[<a href="#ref2" style="color:#520049">2</a>]</sup>.</p>
    
    <div class="sequence">F47-aptamer: 5'-GGGAAGGGAUCCAAUCUACAAAUUCGUUAACAGAAAACCUCAGUUGCUGGGUUGUUUCACUGCAAACUUGACAAAGCUA-3'</div>
    <div class="sequence">F47tr-aptamer: 5'-GGGUUAACAGAAAACCUCAGUUGCUGGGUUGU-3'</div>
    
    <table class="table table-bordered" style="table-layout:fixed;width:1000px;margin-left:auto;margin-right:auto;"><tr>
      <td style="text-align:center;padding-bottom: 0px;padding-left: 0px;padding-top: 0px;padding-right: 0px">
      <img src="/images/2D/3Dpol_aptamer_2D1.svg" alt="drawing" style="width:500px;height:400px;margin-top: 0px;margin-bottom: 0px;" >
      </td>
      <td style="text-align:center;padding-bottom: 0px;padding-right: 0px;padding-top: 0px;padding-right: 0px">
      <img src="/images/2D/3Dpol_aptamer_2D2.svg" alt="drawing" style="width:500px;height:400px;margin-top: 0px;margin-bottom: 0px;" >
      </td>
      </tr>
    </table>
  </div>

  <div class="content-section">
    <h2 class="section-title" id="ligand-recognition">Ligand information</h2>
    
    <div class="blowheader_box">SELEX ligand</div>
    <p>RNA-dependent RNA polymerase (RdRp) or RNA replicase is an enzyme that catalyzes the replication of RNA from an RNA template. Specifically, it catalyzes synthesis of the RNA strand complementary to a given RNA template. This is in contrast to typical DNA-dependent RNA polymerases, which all organisms use to catalyze the transcription of RNA from a DNA template.-----from Wikipedia</p>
    
    <table class="table table-bordered" style="table-layout:fixed;width:1000px;margin-left:auto;margin-right:auto;" >
      <thead>
          <tr>
            <th onclick="sortTable(0)">Name</th>
            <th onclick="sortTable(1)">Uniprot ID</th>
            <th onclick="sortTable(2)">Pfam</th>
            <th onclick="sortTable(3)">MW</th>
            <th onclick="sortTable(4)">Amino acids sequences</th>
            <th onclick="sortTable(5)">PDB</th>
            <th onclick="sortTable(6)">Gene ID</th>
          </tr>
      </thead>
        <tbody>
          <tr>
            <td name="td0">3Dpol</td>
            <td name="td1"><a href="https://www.uniprot.org/uniprotkb/O14227/entry" target="_blank" style="color:#520049"><b>O14227</b></a></td>
            <td name="td2"><a href="https://www.ebi.ac.uk/interpro/entry/pfam/PF00680/" target="_blank" style="color:#520049"><b>PF00680</b></a></td>
            <td name="td3">53.97 kDa</td>
            <td name="td4">GLIVDTRDVEERVHVMRKTKLAPTVAHGVFNPEFGPAALSNKDPRLNEGVVLDEVIFSKHKGDTKMSAEDKALFRRCAADYASRLHSVLGTANAPLSIYEAIKGVDGLDAMEPDTAPGLPWALQGKRRGALIDFENGTVGPEVEAALKLMEKREYKFACQTFLKDEIRPMEKVRAGKTRIVDVLPVEHILYTRMMIGRFCAQMHSNNGPQIGSAVGCNPDVDWQRFGTHFAQYRNVWDVDYSAFDANHCSDAMNIMFEEVFRTEFGFHPNAEWILKTLVNTEHAYENKRITVEGGMPSGCSATSIINTILNNIYVLYALRRHYEGVELDTYTMISYGDDIVVASDYDLDFEALKPHFKSLGQTITPADKSDKGFVLGHSITDVTFLKRHFHMDYGTGFYKPVMASKTLEAILSFARRGTIQEKLISVAGLAVHSGPDEYRRLFEPFQGLFEIPSYRSLYLRWVNAVCGDAAALEHHHHHH</td>
            <td name="td5"><a href="https://www.rcsb.org/structure/8C2P" target="_blank" style="color:#520049"><b>8C2P</b></a></td>
            <td name="td6"><a href="https://www.ncbi.nlm.nih.gov/protein/BBB93554.1" target="_blank" style="color:#520049"><b>BBB93554.1</b></a></td>
          </tr>
        </tbody>
    </table>

    <p>Some isolated sequences bind to the affinity of the protein.</p>
    <table class="table table-bordered" style="table-layout:fixed;width:1000px;margin-left:auto;margin-right:auto;" >
      <thead>
          <tr>
            <th onclick="sortTable(0)">Name</th>
            <th onclick="sortTable(1)">Sequence</th>
            <th onclick="sortTable(2)">Ligand</th>
            <th onclick="sortTable(3)">Affinity</th>
          </tr>
      </thead>
        <tbody>
          <tr>
            <td name="td0">F47-aptamer</td>
            <td name="td1">5'-GGGAAGGGAUCCAAUCUACAAAUUCGUUAACAGAAAACCUCAGUUGCUGGGUUGUUUCACUGCAAACUUGACAAAGCUA-3'</td>
            <td name="td2">3Dpol</td>
            <td name="td3">18 nM</td>
          </tr>
          <tr>
            <td name="td0">F47tr-aptamer</td>
            <td name="td1">5'-GGGUUAACAGAAAACCUCAGUUGCUGGGUUGU-3'</td>
            <td name="td2">3Dpol</td>
            <td name="td3">14 nM</td>
          </tr>
        </tbody>
    </table>
    <div style="display: flex; justify-content: center;"></div>
    <img src="/images/SELEX_ligand/3Dpol_SELEX_ligand.svg" alt="drawing" style="width:1000px;border:solid 1px #efefef;display:block;margin:0 auto;border-radius:0;" class="img-responsive">
    <div style="display: flex; justify-content: center;"></div>

    <div class="blowheader_box">Similar compound</div>                    
    <p>We used the Dail server website to compare the structural similarities of ligand proteins, and chose the top 10 in terms of similarity for presentation. The Dali server is a network service for comparing protein structures in 3D. Dali compares them against those in the Protein Data Bank (PDB). Z-score is a standard score that is converted from an original score. The list of neighbours is sorted by Z-score. Similarities with a Z-score lower than 2 are spurious. RMSD(Root Mean Square Deviation) value is used to measure the degree to which atoms deviate from the alignment position.</p>
    
    <table class="table table-bordered" style="table-layout:fixed;width:1000px;margin-left:auto;margin-right:auto;">
      <thead>
        <tr>
          <th onclick="sortTable(0)">PDB</th>
          <th onclick="sortTable(1)">Z-socre</th>
          <th onclick="sortTable(2)">RMSD</th>
          <th onclick="sortTable(3)">Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td name="td0">2IJD-1</td>
          <td name="td1">42.5</td>
          <td name="td2">1.9</td>
          <td name="td3">Picornain 3c, rna-directed rna polymerase</td>
        </tr>
                
        <tr>
          <td name="td0">1SH0-B</td>
          <td name="td1">33.2</td>
          <td name="td2">2.7</td>
          <td name="td3">Picornain 3c, rna-directed rna polymerase</td>
        </tr>
                
        <tr>
          <td name="td0">5Y6R-A</td>
          <td name="td1">25.7</td>
          <td name="td2">3.2</td>
          <td name="td3">Genome polyprotein</td>
        </tr>
                
        <tr>
          <td name="td0">8WU3-B</td>
          <td name="td1">24.9</td>
          <td name="td2">3.2</td>
          <td name="td3">Rna polymerase</td>
        </tr>
                
        <tr>
          <td name="td0">8IIC-B</td>
          <td name="td1">24.4</td>
          <td name="td2">2.6</td>
          <td name="td3">Polymerase polyprotein</td>
        </tr>
                
        <tr>
          <td name="td0">4K6M-A</td>
          <td name="td1">23.9</td>
          <td name="td2">3.0</td>
          <td name="td3">Rna-directed rna polymerase</td>
        </tr>
                
        <tr>
          <td name="td0">3GNW-B</td>
          <td name="td1">23.6</td>
          <td name="td2">3.3</td>
          <td name="td3">Potential rna-dependent rna polymerase</td>
        </tr>
                
        <tr>
          <td name="td0">5I61-A</td>
          <td name="td1">21.6</td>
          <td name="td2">2.9</td>
          <td name="td3">Rna-directed rna polymerase</td>
        </tr>
                
        <tr>
          <td name="td0">8GWE-A</td>
          <td name="td1">20.5</td>
          <td name="td2">3.0</td>
          <td name="td3">Rna-directed rna polymerase</td>
        </tr>
                
        <tr>
          <td name="td0">1HHS-A</td>
          <td name="td1">16.6</td>
          <td name="td2">3.5</td>
          <td name="td3">Rna-directed rna polymerase</td>
        </tr>
      </tbody>
    </table>
  </div>
                 
  <div class="content-section">
    <h2 class="section-title" id="references">References</h2>
                    
    <a id="ref1"></a><font><strong>[1] Structure of foot-and-mouth disease virus RNA-dependent RNA polymerase and its complex with a template-primer RNA.</strong></font><br />
    Ferrer-Orta,& Verdaguer, N.<br />
    <a href="https://pubmed.ncbi.nlm.nih.gov/15294895/" target="_blank" style="color:#520049">The Journal of biological chemistry, 279(45), 47212–47221. (2004)</a>
    <br/>

    <a id="ref2"></a><font><strong>[2] Selection and characterization of RNA aptamers to the RNA-dependent RNA polymerase from foot-and-mouth disease virus.</strong></font><br />
    Ellingham, M., & Stonehouse, N. J.<br />
    <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1624902/" target="_blank" style="color:#520049">RNA (New York, N.Y.), 12(11), 1970–1979. (2006)</a>
    <br/>
  </div>

  <!-- 保留原有的Molstar查看器脚本 -->
  <script>
    window.addEventListener('DOMContentLoaded', function() {
      var td = document.getElementsByName('td4')[0];
      var maxLength = 100; // 设置最大长度
      var originalText = td.innerHTML;
      var displayedText = originalText.substring(0, maxLength);
      
      if (originalText.length > maxLength) {
        displayedText += '<span class="ellipsis-btn">......</span>'; // 在超出长度时添加省略号按钮
        displayedText += '<span class="hidden-content">' + originalText.substring(maxLength) + '</span>'; // 隐藏的内容
        td.innerHTML = displayedText;
        
        // 获取省略号按钮元素和隐藏的内容元素
        var ellipsisBtn = td.querySelector('.ellipsis-btn');
        var hiddenContent = td.querySelector('.hidden-content');
        
        // 添加点击事件监听器
        ellipsisBtn.addEventListener('click', function() {
          if (hiddenContent.style.display === 'none') {
            hiddenContent.style.display = 'inline'; // 展开内容
            ellipsisBtn.innerHTML = '...'; // 更新按钮文字为"..."
            td.appendChild(ellipsisBtn); // 将按钮移到内容后面
          } else {
            hiddenContent.style.display = 'none'; // 收起内容
            ellipsisBtn.innerHTML = '......'; // 更新按钮文字为省略号
            td.appendChild(ellipsisBtn); // 将按钮移到内容后面
          }
        });
      }
    });
  </script>
</body>
</html>
