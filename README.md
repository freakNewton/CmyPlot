# CmyPlot  
**Data Visualisation Web App**  
  


![GitHub](https://img.shields.io/github/license/thosaniparth/Cmyplot)
[![DOI](https://zenodo.org/badge/418669581.svg)](https://zenodo.org/badge/latestdoi/418669581)
![GitHub issues](https://img.shields.io/github/issues-raw/thosaniparth/Cmyplot)
![Github closes issues](https://img.shields.io/github/issues-closed-raw/thosaniparth/Cmyplot)
[![codecov](https://codecov.io/gh/thosaniparth/CmyPlot/branch/main/graph/badge.svg?token=MFMBV2TFF3)](https://codecov.io/gh/thosaniparth/CmyPlot)

## Why Data Visualization?

With enormous data in hand you would always want to visualize it for good understanding and better clarity with minimal efforts. 

As the famous saying goes - `"The greatest value of visualization is when it forces us to notice what we never expected to see"` - John W. Tukey

`CmyPlot` is a web app that provides interface for uploading a csv data file and convert it into Tables and interesting graphs with one click

- ## Built with

  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" height="40" />
  <img src="docs/images/custom_icons/plotly_icon.png" width="40" height="40"/>
  <img src = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" width="40" height="40"/>

- **Language used:** Python
- **Libraries used:** Flask, Plotly, Dash

## Important Links
1. [User Story Board and Project Vision](https://github.com/thosaniparth/CmyPlot/wiki/User-Story-Board-and-Project-Vision)
2. You can view the web app here [CmyPlot](https://cmyplot-seproject.herokuapp.com) !!
3. How Phase 2 is improved from Phase 1 - [Checkout here](https://github.com/thosaniparth/CmyPlot/blob/main/docs/SE%20Phase%202%20-%20How%20this%20version%20improves%20on%20the%20older%20version.pdf)
4. [Project Phase 2 Rubrics](https://github.com/thosaniparth/CmyPlot/blob/main/proj2rubric.md)
5. [Instructions](#Instructions)
6. What's new in [Phase 2](#Phase2)?
7. [Future Scope](#FutureScope)
8. [Team Members](#TeamMember)

## Visual Walkthrough: 

## Phase 1
https://user-images.githubusercontent.com/65619749/134620802-5fac9f0e-d697-49df-876c-3f5ff7d86e38.mp4

## Phase 2
https://user-images.githubusercontent.com/89279195/140425356-148bc24a-96bd-4ec0-a380-b2bc2cdc2bd0.mp4


## Quick look:

<table border="2" bordercolorlight="#b9dcff" bordercolordark="#006fdd">

  <tr style="background: #010203 ">
    <td valign="left"> 
      <p style="color: #FF7A59"> 1.This is the authentication for using CmyPlot 
      </p>
      <a href="./docs/images/authentication_usr_pwd.png"> 
        <img src="./docs/images/authentication_usr_pwd.png" >      
      </a>
    </td>
    <td valign="left"> 
      <p style="color: #FF7A59"> 2.This is the main Cmyplot web page
      </p>
      <a href="./docs/images/home_page.png">
        <img src="./docs/images/home_page.png"> 
      </a>
    </td>
  </tr>

<table border="2" bordercolorlight="#b9dcff" bordercolordark="#006fdd">

  <tr style="background: #010203 ">
    <td valign="left"> 
      <p style="color: #FF7A59"> 3.You have an option to upload your csv file 
        by Drag and drop or click 
      </p>
      <a href="./docs/images/pre_upload.png"> 
        <img src="./docs/images/pre_upload.png" >      
      </a>
    </td>
    <td valign="left"> 
      <p style="color: #FF7A59"> 4.You have an option to upload your csv file 
        by Drag and drop or click
      </p>
      <a href="./docs/images/post_upload.png">
        <img src="./docs/images/post_upload.png"> 
      </a>
    </td>
  </tr>
  
  <tr style="background: #010203;"> 
    <td valign="left">
      <p style="color: #FF7A59"> 5.You have an option to upload your csv file 
        by Drag and drop or click
      </p>  
      <a href="./docs/images/table.png">
        <img src="./docs/images/table.png">    
      </a>
    </td>
    <td valign="left"> 
      <p style="color: #FF7A59"> 6.For table, you could use 
      number of rows you want to display per page
      </p>
      <a href="./docs/images/row_count_table.png">
        <img src="./docs/images/row_count_table.png">          
      </a>
    </td>

  </tr> 
  
  <tr style="background: #010203;"> 
    <td valign="left">
     <p style="color: #FF7A59"> 7.Table representation of the data
      </p>
     <a href="./docs/images/table_filtered.png">
        <img src="./docs/images/table_filtered.png"> 
      </a> 
    </td> 
    <td valign="left">
     <p style="color: #FF7A59"> 8.Graph representation of the data
      </p>
     <a href="./docs/images/graph_filled.png">
        <img src="./docs/images/graph_filled.png"> 
      </a> 
    </td> 
  </tr> 
  
  <tr style="background: #010203;"> 
    <td valign="left">
     <p style="color: #FF7A59"> 9.Data information - Mean, Median, Standard Deviation
      </p>
     <a href="./docs/images/graph_information.png">
        <img src="./docs/images/graph_information.png"> 
      </a> 
    </td> 
    <td valign="left">
     <p style="color: #FF7A59"> 10.Data attributes to be displayed in tooltip
      </p>
     <a href="./docs/images/hover_options.png">
        <img src="./docs/images/hover_options.png"> 
      </a> 
    </td> 
  </tr> 
  
  <tr style="background: #010203;"> 
    <td valign="left">
     <p style="color: #FF7A59"> 11.You can select graph type from the filters - Bar chart
      </p>
     <a href="./docs/images/barchart.png">
        <img src="./docs/images/barchart.png"> 
      </a> 
    </td> 
    <td valign="left">
     <p style="color: #FF7A59"> 12.You can select graph type from the filters - Line chart
      </p>
     <a href="./docs/images/linechart.png">
        <img src="./docs/images/linechart.png"> 
      </a> 
    </td> 
  </tr> 
  
  <tr style="background: #010203;"> 
    <td valign="left">
     <p style="color: #FF7A59"> 13.Share graph via email with a message
      </p>
     <a href="./docs/images/email.jpg">
        <img src="./docs/images/email.jpg"> 
      </a> 
    </td> 
    <td valign="left">
     <p style="color: #FF7A59"> 14.Email
      </p>
     <a href="./docs/images/share_graph.png">
        <img src="./docs/images/share_graph.png"> 
      </a> 
    </td> 
  </tr> 


  <!-- <tr style="background: #010203;"> 
    <td valign = "center">
      <a href="./docs/images/graph_filled.png">
        <img src="./docs/images/graph_filled.png"> 
      </a>
    </td>
    
  </tr>  -->
 </table>
   
## Getting started:

  - ### Prerequisite: 
      - Download [Python3.x](https://www.python.org/downloads/) on your system.

   - ### Installation:
      E.g If you downloaded `Python 3.9.7` above, then

      **Steps to setup virtual environment**
     - Create a virtual environment:

        `python3.9 -m venv project1_env`
    
     - Activate the virtual environment: 

        `source project1_env/bin/activate`
    
     - Build the virtual environment:(must be present in project directory)

        `pip install -r requirements.txt`

  - ### Run Instructions <a name="Instructions">

     **To run/test the site locally:**

     - Clone [this (CmyPlot) github repo](https://github.com/thosaniparth/CmyPlot).

     - Navigate to project directory.

     - Create a virtual environment:

        `python -m venv project1_env`
    
     - Activate the virtual environment: 

        `source project1_env/bin/activate`
    
     - Build the virtual environment:

        `pip install -r requirements.txt`

     - Install CmyPlot as package, this step is required due to the testing framework:

        `pip install -e .`
  
     - Run:
     
        `python src/plotting/index.py`

     - Site will be hosted at:
     
        `http://127.0.0.1:8085/`
       
## What's new in Phase 2? <a name="Phase2">
  - Implemented Collaborative Work - Sharing of the images of plots to other users via email
  - Support for more graphs in the application - Added Line, Bar Graphs
  - Informative Graphs - Added more information to the graphs such as central tendencies 
  - Implemented Authentication - Added method for authenticating the users via user name and password
  - Additional details on the hover of the graph - Users can select columns to view and get data on hover of the points on the graph
  - Dynamic rows on pages - Users can select the number of rows they want to see on a particular page and also can change the number of pages
  ## Roadmap <a name="FutureScope">
   - [List of Roadmap and their corresponding open issues](https://github.com/thosaniparth/CmyPlot/issues/21)
       
## Team Members <a name="TeamMember"></a>
[Simran Bosamiya](https://github.com/BosamiyaSimran)

[Nisarg Shah](https://github.com/freakNewton)

[Parth Thosani](https://github.com/thosaniparth)
  
[Parth Jinturkar](https://github.com/ParthJinturkar)


