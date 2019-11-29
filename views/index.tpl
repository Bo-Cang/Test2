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
<form>
<input class="form-control btn-default"
       style="float: left; width: 60%;" type="text" name="keyword"
        placeholder="Keywords" value="{{keyword}}">
   <button class="btn btn-primary" type="submit" >Submit</button>
</form>
</html>
