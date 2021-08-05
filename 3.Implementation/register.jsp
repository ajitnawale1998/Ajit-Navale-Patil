<%@include file="header.jsp" %>
<%@include file="navigation.jsp" %>
<%@include file="flash.jsp" %>

<div class="container">
    <div class="row background space20">
        <div class="span12">
            <form class="form-signin" action="Register" method="post">
                <h2 class="form-signin-heading">Register</h2>
                <label class="label label-info label-important">Enter Full name</label>
                <input type="text" class="input-block-level validate[required]" placeholder="full name" name="fullname"/>
                <span class="label label-info">Enter User name</span>
                <input type="text" class="input-block-level validate[required]" maxlength="8" placeholder="username" name="username"/>
                <span class="label label-info">Enter Password</span>
                <input type="password" class="input-block-level validate[required]" placeholder="password" name="password"/>
                <label class="label label-info label-important">Enter Address</label>     
                <input type="text" class="input-block-level validate[required]" placeholder="address" name="address"/>
                <span class="label label-info">Email Address</span>
                <input type="email" class="input-block-level validate[required, custom[email]]" placeholder="Email Address" name="email"/>
                <span class="label label-info">Enter Phone number</span>
                <input type="number" class="input-block-level validate[required, custom[phone]]" placeholder="Phone Number" name="contact"/>
                <button align="middle" class="btn btn-large btn-primary" type="submit" align="center" >Register</button>
            </form>
        </div>

    </div>

    <!-- Example row of columns -->
</div>
<%@include file="footer.jsp" %>