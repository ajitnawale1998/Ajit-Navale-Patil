Abstract:-
       The main goal of these system is to achieve maximum yield rate of crop using land resource.
Selection of crop yield is maximized by considering the proportion of nutrients present in the soil. In
this system, the farmer / beginner will classify and predict the crop cultivation based on their weather,
monsoon and soil type along with their pH level.For classification we have used the Random Forest
algorithm .for the chosen crop, the cultivation process is recommended in the form of text and video.
During the cultivation of crops,the amount of fertilizers, insecticides and fungicides are analyzed
using Machine Learning Technique. Here,Random Forest Algorithm is used for classification and
prediction of crops and K-Nearest Neighbor Algorithm is used for recommending nearby shops using
adjacent maps for buying and selling products to the farmers. Finally, using this system the farmers
will have a well guided approach to begin with farming.


Architecture:-

![image](https://user-images.githubusercontent.com/68458509/128523019-1743e6e2-4be0-4b28-ac21-14edf77bcd50.png)
            The System architecture consist 6 modules first is farmers and dealers which will log in into the
system by registering their details. As soon as registration is completed, the admin will store their
details in DB. With the help of AI, the weather can be predicted for the next few days. The farmer will
enter the sand and monsoon type as an input if the given data is trained the RFA will make a decision by categorizing the sand quality into low, medium and high to classify the crops. This classification
is based on the pH level of the soil. The classified crops will be processed parallel to predict and
recommend the best result to the farmers for better cultivation. In case, if there is no match in the
trained dataset that particular input should be feed in the suggestion box for updating. The system
will analyze the symptoms to indicate the disease present in the crop with the help of the ML and
suggest corresponding pesticides, fungicides as a solution for maintaining the health of crop. The
KNN is used to show the nearby shops in the maps to both farmers and dealers for buying and selling
the products.



