+++
date = "2017-04-10T16:40:43+01:00"
title = "Tables"
draft = false
weight = 50
description = "Rows and columns for all sorts of tables"
toc = true
bref = "Tables are an essential part of many different contexts. Kube serves them all and delivers full variety of tables, preformatted to save you time. Whatever your requirements are, tables are completely customizable to match them."
+++

<h3 class="section-head" id="h-base"><a href="#h-base">Base</a></h3>
<div class="example">
  <table>
    <thead>
      <tr>
        <th>First Name</th>
        <th>Last Name</th>
        <th>Points</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Jill</td>
        <td>Smith</td>
        <td>50</td>
      </tr>
      <tr>
        <td>Eve</td>
        <td>Jackson</td>
        <td>94</td>
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <td colspan="2">Total points</td>
        <td>223</td>
      </tr>
    </tfoot>
  </table>
  <pre class="code">&lt;<span class="hljs-keyword">table</span>&gt;...&lt;/<span class="hljs-keyword">table</span>&gt;</pre>
</div>
<h3 class="section-head" id="h-bordered"><a href="#h-bordered">Bordered</a></h3>
<div class="example">
  <table class="bordered">
    <thead>
      <tr>
        <th>First Name</th>
        <th>Last Name</th>
        <th>Points</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Jill</td>
        <td>Smith</td>
        <td>50</td>
      </tr>
      <tr>
        <td>Eve</td>
        <td>Jackson</td>
        <td>94</td>
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <td colspan="2">Total points</td>
        <td>223</td>
      </tr>
    </tfoot>
  </table>
  <pre class="code">&lt;<span class="hljs-keyword">table</span> <span class="hljs-keyword">class</span>=<span class="hljs-string">"bordered"</span>&gt;...&lt;/<span class="hljs-keyword">table</span>&gt;</pre>
</div>
<h3 class="section-head" id="h-striped"><a href="#h-striped">Striped</a></h3>
<div class="example">
  <table class="striped">
    <thead>
      <tr>
        <th>First Name</th>
        <th>Last Name</th>
        <th>Points</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Jill</td>
        <td>Smith</td>
        <td>50</td>
      </tr>
      <tr>
        <td>Eve</td>
        <td>Jackson</td>
        <td>94</td>
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <td colspan="2">Total points</td>
        <td>223</td>
      </tr>
    </tfoot>
  </table>
  <pre class="code">&lt;<span class="hljs-keyword">table</span> <span class="hljs-keyword">class</span>=<span class="hljs-string">"striped"</span>&gt;...&lt;/<span class="hljs-keyword">table</span>&gt;</pre>
</div>
<h3 class="section-head" id="h-unstyled"><a href="#h-unstyled">Unstyled</a></h3>
<div class="example">
  <table class="unstyled">
    <thead>
      <tr>
        <th>First Name</th>
        <th>Last Name</th>
        <th>Points</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Jill</td>
        <td>Smith</td>
        <td>50</td>
      </tr>
      <tr>
        <td>Eve</td>
        <td>Jackson</td>
        <td>94</td>
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <td colspan="2">Total points</td>
        <td>223</td>
      </tr>
    </tfoot>
  </table>
  <pre class="code">&lt;<span class="hljs-keyword">table</span> <span class="hljs-keyword">class</span>=<span class="hljs-string">"unstyled"</span>&gt;...&lt;/<span class="hljs-keyword">table</span>&gt;</pre>
</div>
<h3 class="section-head" id="h-mixed"><a href="#h-mixed">Mixed</a></h3>
<div class="example">
  <table class="bordered striped">
    <thead>
      <tr>
        <th>First Name</th>
        <th>Last Name</th>
        <th>Points</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Jill</td>
        <td>Smith</td>
        <td>50</td>
      </tr>
      <tr>
        <td>Eve</td>
        <td>Jackson</td>
        <td>94</td>
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <td colspan="2">Total points</td>
        <td>223</td>
      </tr>
    </tfoot>
  </table>
  <pre class="code">&lt;<span class="hljs-keyword">table</span> <span class="hljs-keyword">class</span>=<span class="hljs-string">"bordered striped"</span>&gt;...&lt;/<span class="hljs-keyword">table</span>&gt;</pre>
</div>
<h3 class="section-head" id="h-width"><a href="#h-width">Width</a></h3>
<div class="example">
  <table class="bordered">
    <thead>
      <tr>
        <th class="w40">First Name</th>
        <th class="w40">Last Name</th>
        <th class="w20">Points</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Jill</td>
        <td>Smith</td>
        <td>50</td>
      </tr>
      <tr>
        <td>Eve</td>
        <td>Jackson</td>
        <td>94</td>
      </tr>
    </tbody>
  </table>
  <pre class="code"><span class="hljs-tag">&lt;<span class="hljs-name">table</span>&gt;</span>
<span class="hljs-tag">&lt;<span class="hljs-name">tr</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-name">td</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"w40"</span>&gt;</span>...<span class="hljs-tag">&lt;/<span class="hljs-name">td</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-name">td</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"w40"</span>&gt;</span>...<span class="hljs-tag">&lt;/<span class="hljs-name">td</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-name">td</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"w20"</span>&gt;</span>...<span class="hljs-tag">&lt;/<span class="hljs-name">td</span>&gt;</span>
<span class="hljs-tag">&lt;/<span class="hljs-name">tr</span>&gt;</span>
<span class="hljs-tag">&lt;/<span class="hljs-name">table</span>&gt;</span></pre>
<table class="table table-bordered table-hover table-condensed">
<thead><tr><th title="Field #1">Person - Name</th>
<th title="Field #2">Person - Organization</th>
<th title="Field #3">Person - Email</th>
</tr></thead>
<tbody><tr>
<td>John Meekins</td>
<td>Florida Department of Corrections</td>
<td>john.meekins@fdc.myflorida.com</td>
</tr>
<tr>
<td>Derek Snider</td>
<td>Uncharted</td>
<td>derektest@uncharted.software, dsnider@uncharted.software</td>
</tr>
<tr>
<td>Jason Slepicka</td>
<td>University of Southern California (USC) Information Sciences Institute (ISI)</td>
<td>slepicka@isi.edu</td>
</tr>
<tr>
<td>dmorrissey sacsheriffcom</td>
<td>Sacramento County Sheriff&#39;s Department (California)</td>
<td>dmorrissey@sacsheriff.com</td>
</tr>
<tr>
<td>Alberto Lopez</td>
<td>City of Anaheim</td>
<td>alblopez@anaheim.net</td>
</tr>
<tr>
<td>Lianne Binckes</td>
<td>Homeland Security Investigations (DHS ICE HSI)</td>
<td>lianne.s.binckes@ice.dhs.gov</td>
</tr>
<tr>
<td>Christopher Sharp</td>
<td>Department of Justice (DOJ)</td>
<td>christopher.c.sharp@usdoj.gov</td>
</tr>
</tbody></table>


</div>
