<html>
   <head>
      <h1>hello world</h1>
      % for i in range(10):
      <p>This is the loop {{i}}</p>
      % end
    </head>
<div class="jumbotron text-center" style="margin-bottom:0">
  <h1>MySearcher</h1>
  <p>Please enter the keyword</p>
</div>
<body>

    <form method="post" action="q">
        <div>
            <label for="name">Keyword:</label>
            <input type="text" id="name" name="keyword">
        </div>
        <button type="submit">Submit</button>
    </form>
<table class="table">
    % if not page_list:

    <tr>
    <td>
        <br>
        <br>
        <h2>Do not find any similar data</h2>
        <br>
        <br>
    </td>
    </tr>
    % end

   %for page in page_list:
    <tr>
    <td>
        <a class="btn-light" target="view_window" href="{{page[1]}}">
            {{page[3]}}
        </a>
        <br>
        <br>
        {{page[2]}}
        <br>
        <br>
    </td>
    </tr>
   %end
</table>
</body>
</html>
