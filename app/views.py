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
        <textarea id="repl" name="code" rows="1" cols="80" ></textarea>
    </div>
    </html>

    <script type="text/javascript">
        $('#repl').bind('keypress', function(e) {
            if (e.keyCode == 13) {
                $.ajax({
                    url: '/parse',
                    data: {lines: $("#repl").val()},
                    success: function(rslt) {
                        $("#main").append('>'+$("#repl").val());
                        $("#main").append(rslt);
                        var el = $("#repl");
                        el.val('');
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
