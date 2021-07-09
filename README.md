# Peter Lynch Photography

## Description

This is a photo gallery website that displays photographs taken by a friend of mines. The images are displayed in rows of 4 with continuous columns. Users are able to hover over and click on an image to bring up a larger version of the image. Users can scroll through the images by pressing either the right and left arrows, or by clicking on the arrows on each side of the image. The photographer's social media profiles are connected to icons at the top of the page.

## Wireframes

I have used Figma to create the wireframes: [Click here](https://github.com/terencecistudent/peters-portfolio/blob/master/wireframes/peterlynchphotography.pdf)

## UX

### User Stories:

#### Implemented:

1. As a user, I would like to see the images displayed in a nice format.

- **End User Goal**: User is able to upload the website with the styles being applied for the images to be displayed nicely.
- **End Business Goal**: Images displaying in a nice format.
- **Acceptance Criteria**: Images displaying in a nice format due to the styles from the stylesheet.
- **Measures Of Success**: Check Manual Tests.

2. As a user, I would like to click on an image which will then bring up a bigger version of that image.

- **End User Goal**: User is able to click on any image which will then show a bigger version of that image.
- **End Business Goal**: Images to be displayed in a larger format when clicked on.
- **Acceptance Criteria**: Images to be displayed in a larger format when clicked on.
- **Measures Of Success**: User is able to clock on an image which then brings up a bigger version of that image. Check Manual Tests.

3. As a user, I would like to scroll through the images.

- **End User Goal**: User is able to scroll through all of the images.
- **End Business Goal**: Users are able to scroll through all of the images.
- **Acceptance Criteria**: Users are able to scroll through all of the images.
- **Measures Of Success**: User is able to scroll through the images. Check Manual Tests.

4. As a user, I would like to X off the bigger version of an image that I clicked on.

- **End User Goal**: User is able to X off a particular or any image by clicking the X icon below the image.
- **End Business Goal**: Users to have simple navigation to X off an image by clicking on the X icon below the image.
- **Acceptance Criteria**: Users to be able to click off an image using the X icon.
- **Measures Of Success**: User is able to click off the image by pressing the X icon. Check Manual Tests.

5. As a user, I would like to click on any of the social media icons where I should be directed to that social media page.

- **End User Goal**: User is able to click on any social media icon which directs them to the correct page.
- **End Business Goal**: Users are able to click on any of the social media icons where they are directed to the correct pages.
- **Acceptance Criteria**: Users are able to click on any of the social media icons where they are directed to the correct pages.
- **Measures Of Success**: User is directed to the correct social media pages.

## Framework

For the styling side of the website, I have decided to use Bootstrap 4. As Bootstrap is a mobile first framework, this is suitable for this website as users do not need to be on a laptop or computer to see the website properly. Users can view the website using their mobiles and still access the images.

I have used the Flask framework to help loop through the images folder. I felt that if the client wanted to expand upon his website, then Flask would be suitable due to the jinja templates and routing.

## Requirements

- Access to a desktop, laptop, tablet and mobile devices.
- Internet connection.

## Features

- **Images**: Users can click and scroll through the images.
- **Social Media Icons**: Users can click on any of the social media icons which directs them to a social media profile page.

## Deployment

### Custom Domain Name:

Although I have deployed this website using Heroku, I have implemented a custom domain name which I purchased from [GoDaddy](https://uk.godaddy.com).

I watched this video from Dennis Ivy to help with the DNS settings to connect the domain name from GoDaddy to Heroku: [Click here](https://www.youtube.com/watch?v=CxrzD73r6Rw&t=569s).

This application was deployed using Heroku which can be viewed from here: [Peter Lynch Photography](https://www.peterlynch-photography.com)

I have used VS Code to help develop this website. This was pushed to Heroku through the command line by linking the master git from my remote GitHub repository to a new app created in Heroku.

There are no differences between the website's development version and the deployed version to Heroku.

### Deploying to Heroku:

1. Go to the Heroku website [here](https://id.heroku.com/login).

2. Sign Up or Sign In which will direct you to the dashboard.

3. Click on **New > Create new app**.

4. Enter app name and choose region then press **Create App**.

5. In the CLI, login into Heroku by **heroku login -i**, where you will be asked to your enter email address and password.

6. If you have already created your Heroku app, you can remote to your local repository with the heroku git:remote command.

7. Set debug=False for deployment.

8. To deploy your app to Heroku, use the git push command to push the code from your local repository’s master branch to
   your heroku remote:

   ![image](https://user-images.githubusercontent.com/48124466/76408974-ae0b5580-6385-11ea-9cf1-8d67c4f0dff5.png)

9. When the build is complete, on the Heroku website, in the app click **Open App**.

[Deploying with Git](https://devcenter.heroku.com/articles/git)

## Testing

### Manual Tests:

I have carried out manual tests on User Stories No. 1-4.

[Manual Tests](https://github.com/terencecistudent/peters-portfolio/blob/master/testing/Manual%20Tests.pdf)

### Responsiveness On Different Devices Tests:

I have done tests of the website's responsiveness using both Google Chrome's and Microsoft Edge's Dev Tools.

[Responsive Tests](https://github.com/terencecistudent/peters-portfolio/blob/master/testing/Responsiveness-On-Different-Devices.pdf)

### Running Responsive Designs on Google Chrome:

Here is a link how to run the application on a live server by configuring and exposing ports with GitPod:
https://www.gitpod.io/docs/43_config_ports/

**To view responsive applications:**

1. Right click then go to **Inspect Element**.
2. Click on the **Toggle Device Toolbar** (Icons showing two devices):
   ![image](https://user-images.githubusercontent.com/48124466/68051275-f2ebf500-fcde-11e9-8b3a-adc7abc16c5f.png)
3. Click on any device, for example, iPhone 5/SE selected:
   ![image](https://user-images.githubusercontent.com/48124466/68051467-5aa24000-fcdf-11e9-8666-d29f1afa8955.png)

### Code Validation:

- HTML
  - is validated using [W3 validator](https://validator.w3.org/).
- CSS
  - is validated using [W3 Jigsaw](https://jigsaw.w3.org/css-validator/).
- Python
  - is validated using [Pep8Online](http://pep8online.com/).

## Technologies Used

### Languages:

- HTML5
  - Used for the structure and layout.
- CSS3
  - Used for the styling of the wesbsite.
- JavaScript
  - Used to implement lightbox structure.
- Python
  - Used to loop through images folder.

### README.md:

- Markdown
  - Used for the README.md file.

### Frameworks:

- Bootstrap v4.3.1
  - This framework is used in this appplication for:
    - Navbar
    - Styling
    - Responsive Layouts
    - Image Layouts
- Flask Framework v1.1.2
  - Is a Python framework that encourages rapid development.

### Libraries:

- Font Awesome
  - Font Awesome Icons were used throughout the website.
- jQuery
  - Used to help simplify HTML DOM tree traversal and manipulation.
- Google Fonts
  - Helped with the visibility of the text for users to see clearly.

### Others:

- Git
  - Version control to the GitHub repositories.
  - Ran the code to expose a live port.
- GitHub
  - Remote repository.
- Google Chrome Developer Tools
  - Helped with small changes.

## Cloning and Pushing To The Respository

### Cloning:

- Here is a link how to clone a repository:
  https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository

### Pushing To The Respository:

- To add, commit and push files to the repository, e.g. index.html, open a New Terminal and type:

1. git add index.html
2. git commit -m "Leave a message here"
3. git push origin master - (which is for the master branch).

- To create a new branch within your current application, open a New Terminal:

1. Create a branch: git checkout -b new-branch-name
2. Edit, add to your application and commit the files.
3. Push the branch to the remote repository: git push origin new-branch-name.

## Support

To contact GitHub, follow this link: https://support.github.com/

## Credits:

- **Media**: Peter Lynch's Photographs
- **Author**: Terence Logue
