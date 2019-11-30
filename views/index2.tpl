<html>
   <head>
        <title>BBSearcher</title>

        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

   </head>
   <body>

<div class="jumbotron text-center" style="margin-bottom:0">
  <h1>MySearcher</h1>
  <p>Please enter the keyword</p>
</div>

<form action="/q">
<input class="form-control btn-default"
       style="float: left; width: 60%;" type="text" name="keyword"
        placeholder="Keywords" value="{{keyword}}">
   <button class="btn btn-primary" type="submit" >Submit</button>
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
