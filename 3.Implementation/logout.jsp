<%
    session.setAttribute("User", null);
    session.setAttribute("UserType", null);
//String user=session.getAttribute("User").toString();
//out.println(user);

    session.setAttribute("flash_message", "logged out successfully !!!");
//    session.setAttribute("flash_message", user);
    session.setAttribute("flash_type", "info");


    session.invalidate();
    response.sendRedirect("index.jsp");



%>

