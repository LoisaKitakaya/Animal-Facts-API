$(document).ready(function () {
  var jsbtn = $(".js");
  var jqbtn = $(".jq");
  var pybtn = $(".py");

  //
  var jscode = $(".js-snippet");
  var jqcode = $(".jq-snippet");
  var pycode = $(".py-snippet");

  //
  jqcode.hide();
  pycode.hide();

  jsbtn.click(function () {
    jscode.show();
    jqcode.hide();
    pycode.hide();
  });

  jqbtn.click(function () {
    jqcode.show();
    jscode.hide();
    pycode.hide();
  });

  pybtn.click(function () {
    pycode.show();
    jscode.hide();
    jqcode.hide();
  });
});
