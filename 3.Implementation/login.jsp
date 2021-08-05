<%@include file="header.jsp" %>
<%@include file="navigation.jsp" %>
<%@include file="flash.jsp" %>

<div class="container">

 
  <div class="row background space20">
        <div class="span12">
            <form class="form-signin" action="UserLogin" method="post">
                <h2 class="form-signin-heading">Farmer Login</h2>
                <div id="myTabContent" class="tab-content">
                    <input type="text" class="input-block-level validate[required,minSize[3]]" placeholder="username" name="username" >
                    <input type="password" class="input-block-level validate[required]" placeholder="password" name="password" >
                    <button class="btn btn-large btn-primary" type="submit">Log In</button>
                </div>
            </form>
        </div>
        
    </div>
</div><br/><br/>
<%@include file="footer.jsp" %>