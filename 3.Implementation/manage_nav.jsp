<%@page import="java.lang.String"%>
<%@page import="java.util.HashMap"%>
<ul class="pull-right nav">
    <%
        String userType = (String) session.getAttribute("UserType");
//        System.out.println("userType: " + userType);
        if (userType == null)
        {
    %>
    <li><a href="index.jsp">Home</a></li>
    <li><a href="login_admin.jsp">Admin login</a></li>
        <li><a href="login.jsp">Farmer login</a></li>

    <li><a href="register.jsp">Farmer Registration</a></li>
    <% } else {
        if (userType.equals("admin")) {
    %> 
    <li> <a href="fileupload.jsp" >Upload Train Data</a></li>
    <li><a href="ViewDataTrain.jsp">View Train Details</a></li>
    <li> <a href="fileuploadTest.jsp" >Upload Test Data</a></li>
    <li><a href="ViewDatasetTest.jsp">View Test Details</a></li>
    <li> <a href="SelectTraining.jsp" >Execute Training</a></li>
    <li><a href="ViewUsers.jsp">View Users</a></li>
    <li><a href="logout.jsp">logout [Admin] </a></li>
    <%
        }
        else {
    %>
        <li><a href="Input_data.jsp">Enter Input Data</a></li>
    <li><a href="viewPredicedCrops.jsp">View Predicted Crops</a></li>
    <li><a href="logout.jsp">logout [<%= session.getAttribute("username") %>]</a></li>
    <% 
        }
        }
    %>
</ul>