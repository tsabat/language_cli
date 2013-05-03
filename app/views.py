from app import app
from app import request
from app.parser import parse

@app.route('/')
def hello():
    return """
    <html>
    <head>
        <script src="//ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min.js"></script>
    </head>
    <div id="main">
        Type some code.  Press ctrl+enter to run it.<hr>
        <textarea id="repl" name="code" rows="25" cols="80" ></textarea>
    </div>
    </html>

    <script type="text/javascript">
        $('#repl').bind('keypress', function(e) {
            if (e.ctrlKey && (e.keyCode == 13)) {
                $.ajax({
                    url: '/parse',
                    data: {lines: $("#repl").val()},
                    success: function(rslt) {
                        $("#main").append('<pre>>'+$("#repl").val() + '</pre>');
                        $("#main").append(rslt);
                        var el = $("#repl");
                        el.appendTo("#main");
                        el.focus();
                        console.log(rslt);
                    }
                });
                e.preventDefault();
            }});

    </script>
    """

@app.route('/parse')
def route():
    return '<pre>' + parse(request.args.get('lines', '')) + '</pre>'
