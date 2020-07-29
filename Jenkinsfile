import hudson.model.*
pipeline {  
  

   agent any
   

//    tools {
//       // Install the Maven version configured as "M3" and add it to the path.
//      maven "apache-maven-3.6.3" 
//    }

   stages {
    
		// }
	  stage('Build the code') {
		steps{
                echo "building the code from feature-1 branch"
    		}
		}
		//when {
			//expression { "${ArtifactoryUpload} == "true" }
				
			//}
	  stage('Deploy to artifactory') {
		
		  steps{ 
              echo "Saving the build to the artifactoery repo"
		
		  }
	  }
	
    stage ('Deploy to Target Server') {
      steps{
          echo "Deploying the build to the target environment"
       
      }
    } 
  // stage('SonarQube analysis') {
   // steps {
  //   withSonarQubeEnv(credentialsId: 'f225455e-ea59-40fa-8af7-08176e86507a', installationName: 'My SonarQube Server') { 
  //     sh 'mvn org.sonarsource.scanner.maven:sonar-maven-plugin:3.7.0.1746:sonar'
    //}
  //   }
  // }
}

  post {
//always {echo 'I will always say Hello again!'}
    failure {
      echo "FAILURE!!"
    }
    success {
      echo "SUCCESS!!"
    } 
  }
}
   

}





