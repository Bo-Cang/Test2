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
            <label for="name">Name:</label>
            <input type="text" id="name" name="keyword" value="{{keyword}}">
        </div>
        <button type="submit">Submit</button>
    </form>

</body>
</html>
