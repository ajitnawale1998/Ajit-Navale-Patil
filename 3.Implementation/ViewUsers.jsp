<%@include file="header.jsp" %>
<%@include file="navigation.jsp" %>
<%@include file="flash.jsp" %>

<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="core.db.dbconn"%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title></title>
    </head>
    <body>
        <%

            Statement st = null;
            ResultSet rs = null;
            String userid = (String) session.getAttribute("id");
            System.out.println("userid=" + userid);
            try {
                st = dbconn.connect();
                String sql = "select * from users ";
                rs = st.executeQuery(sql);
        %>
        <div class="container">


            <div>
                <table class="table table-hover table-striped">
                    <thead>
                        <tr>
                            <th>Full Name</th>
                            <th>Username</th>
                            <th>Address</th>
                            <th>Email</th>
                            <th>Contact_no</th>
                            <th>Delete</th>
                        </tr>
                    </thead>
                    <tbody>
                        <%while (rs.next()) {
                                String id = rs.getString(1);
                                String full_name = rs.getString(2);
                                String user_name = rs.getString(3);
                                String address = rs.getString(5);
                                String email = rs.getString(6);
                                String contact_no = rs.getString(7);
                        %>
                        <tr>
                            <td>
                                <%= full_name%>
                            </td>
                            <td>
                                <%= user_name%>
                            </td>
                            <td> 
                                <%= address%>
                            </td>
                            <td> 
                                <%= email%>
                            </td>
                            <td> 
                                <%= contact_no%>
                            </td>
                    <td>        
                    <a href="block.jsp?id=<%= id%>" class="btn btn-small btn-danger"></i>Delete</a>
                    </td>     
                    </tr>
                        <% }
                            } catch (Exception e) {
                                e.printStackTrace();
                            }
                        %>
                    </tbody>
                </table>
            </div>
        </div>
    </body>
</html>

<%@include file="footer.jsp" %>