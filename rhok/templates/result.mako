<!doctype html>
<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="en"> <![endif]-->
<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="en"> <![endif]-->
<!--[if IE 8]>    <html class="no-js lt-ie9" lang="en"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en"> <!--<![endif]-->
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <title></title>
  <meta name="description" content="">
  <link rel="stylesheet" href="static/css/bootstrap.min.css">
  <link rel="stylesheet" href="static/css/bootstrap-responsive.min.css">
  <link rel="stylesheet" href="static/css/backbone-forms.css">
  <link rel="stylesheet" href="static/css/ui-lightness/jquery-ui-1.8.20.custom.css">
  <link rel="stylesheet" href="static/css/style.css">
</head>
<body>

<div class="container">
  <header class="row">
    <h1>RHoK Results</h1>
  </header>
  <div class="row" id="Main">
    <table>
      <tr><th>Condition</th><th>Probability</th></tr>
      <tr><td>ASD</td><td>${result['ASD']}</td></tr>
      <tr><td>ADHD</td><td>${result['ADHD']}</td></tr>
      <tr><td>DD</td><td>${result['DD']}</td></tr>
      <tr><td>LI</td><td>${result['LI']}</td></tr>
    </table>
  </div>
</div>

<script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
<script src="static/js/vendor/twitter/bootstrap.min.js"></script>
<script src="static/js/vendor/documentcloud/underscore-min.js"></script>
<script src="static/js/vendor/documentcloud/backbone-min.js"></script>
<script src="static/js/vendor/jquery-ui-1.8.20.custom.min.js"></script>
<script src="static/js/vendor/backbone-forms.js"></script>
<script src="static/js/vendor/jquery-ui-editors.js"></script>


</body>
</html>
