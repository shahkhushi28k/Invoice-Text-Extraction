# Invoice-Text-Extraction

**Introduction**

In today’s digital age, businesses face challenges in efficiently processing invoices due to the manual effort required for data extraction. To address this, automated invoice text extraction using deep learning models like YOLOv5 has emerged as a powerful solution. YOLOv5 offers state-of-the-art object detection capabilities, making it ideal for accurately identifying and extracting text from invoice images.


**Project Overview**

This project focuses on developing an automated system for invoice text extraction using YOLOv5. The system aims to streamline invoice processing workflows by automatically detecting and extracting key information such as invoice numbers, dates, amounts, and vendor details from invoice images. By leveraging YOLOv5's advanced object detection capabilities, the system improves accuracy and efficiency, 
reducing the need for manual intervention in invoice data extraction tasks.


**Key Features**

1. Object Detection with YOLOv5: Utilizes YOLOv5 for precise localization of text regions on invoice images.
2. Text Extraction: Extracts text from identified regions to capture relevant invoice details.
3. Flask Web Application: Provides a user-friendly interface for uploading invoice images and retrieving extracted text information.
4. Integration with VoTT: Uses VoTT (Visual Object Tagging Tool) for labeling invoice images to train the YOLOv5 model.


**Technologies Used**

1. YOLOv5: Deep learning model for object detection and text region localization.
2. Flask: Python web framework used for developing the invoice text extraction system.
3. VoTT (Visual Object Tagging Tool): Tool for labeling invoice images to prepare data for YOLOv5 training.
4. Python: Programming language for backend logic, data processing, and model integration.


**Development Process**

1. Data Labeling with VoTT: Invoice images are labeled using VoTT to annotate text regions required for training the YOLOv5 model.
2. Model Training: YOLOv5 is trained on the annotated dataset, focusing on accurately detecting text regions within invoice images.
3. Flask Application Development: A Flask-based web application is developed to deploy the trained YOLOv5 model. The application allows users to upload invoice images and retrieves extracted text information in a structured format.
4. Testing and Optimization: Extensive testing is conducted to validate the system's accuracy and performance across various invoice formats. Optimization efforts aim to improve text extraction precision and application responsiveness.


**Weekly Report: Invoice Text Extraction Using YOLOv5**

- Week 1: Project Setup and Initial Development
    Day 1-2: Project Initialization and Setup

      Set up the project repository on GitHub.
      Created a README file with project description, objectives, and setup instructions.
      Organized project structure: app.py, train_model.py, and a data folder for invoice images.

    Day 3-4: Data Collection and Preprocessing

      Collected and organized sample invoice images in the data folder.
      Developed a script to preprocess invoice images, preparing them for model training.
  
    Day 5-7: Model Training Preparation

      Explored YOLOv5 and set up environment for training.
      Annotated invoice images using VoTT (Visual Object Tagging Tool) for YOLOv5 training.
      Prepared initial dataset with labeled invoice images.

  ![Screenshot 2024-07-17 221152](https://github.com/user-attachments/assets/713c020d-c2b2-49fe-8422-100f26338696)


    Deliverables:

      Initialized project repository with README.
      Organized and preprocessed sample invoice images.
      Prepared annotated dataset for YOLOv5 model training.
  
**Week 2: Model Training and Web App Development**

    Day 8-10: Model Training

      Trained YOLOv5 on the annotated dataset.
      Optimized model hyperparameters for invoice text extraction.
      
    Day 11-12: Initial Web App Setup

      Set up Flask web application framework (app.py).
      Created basic web interface for uploading invoice images and displaying extraction results.

    Day 13-14: Integrate Model with Web App

      Integrated trained YOLOv5 model with Flask web app.
      Implemented text extraction functionality to extract invoice details from uploaded images.

![Screenshot 2024-07-17 221251](https://github.com/user-attachments/assets/17cbb4e1-8f51-4327-8c1d-f578e5e0257b)


![Screenshot 2024-07-17 221424](https://github.com/user-attachments/assets/c54cb19d-fdd0-4f4f-8824-5c7ed4c40556)

    Deliverables:

      Trained YOLOv5 model for invoice text extraction.
      Initial version of Flask web app with basic functionality.



**Week 3: Feature Enhancement and Testing**

    Day 15-17: Feature Enhancement

      Enhanced web app with additional features: image upload functionality, error handling, and user authentication.
      Improved user interface for better usability and accessibility.
      
    Day 18-19: User Interface and Experience

      Conducted user experience testing and gathered feedback.
      Implemented UI improvements based on user feedback.
      
    Day 20-21: Testing and Debugging

      Conducted rigorous testing of the entire system.
      Addressed bugs and performance issues identified during testing.

    Deliverables:

      Enhanced web app with advanced features and improved UI.
      Conducted comprehensive testing and debugging.
      
**Week 4: Finalization and Deployment**

    Day 22-24: Final Touches

      Optimized YOLOv5 model for speed and accuracy in text extraction.
      Ensured web app responsiveness across different devices.

    Day 25-26: Documentation

      Documented project code, functionalities, and APIs.
      Created user manuals and guides for using the web app.
      
    Day 27-28: Deployment Preparation

      Prepared web app for deployment on cloud platform.
      Tested deployment process to ensure smooth operation.
    
    Day 29-30: Deployment and Final Review

      Deployed web app to production environment.
      Conducted final review and gathered user feedback for further improvements.

    Deliverables:

      Optimized YOLOv5 model and responsive web app.
      Comprehensive project documentation and user guides.
      Deployed web app accessible to users.

**Usage**

To use the Invoice Text Extraction System:

- Clone this repository.
- Install dependencies listed in requirements.txt.
- Run the Flask application (app.py).
- Upload invoice images via the provided web interface to extract text.


**Conclusion**

Developing the Invoice Text Extraction System using YOLOv5 and Flask represents a significant step towards automating invoice processing tasks. By harnessing the power of deep learning and web technologies, businesses can enhance operational efficiency, reduce errors, and improve overall productivity in invoice management workflows.


**Future Enhancements**

1. OCR Integration: Integrate Optical Character Recognition (OCR) to improve text extraction accuracy from detected regions.
2. Multi-format Support: Extend the system's capabilities to handle diverse invoice layouts and formats.
3. Continuous Improvement: Incorporate feedback mechanisms to refine the model's performance and adapt to new invoice variations over time.
