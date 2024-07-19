# Mask Wear Detector

## Overview

The Mask Wear Detector project leverages state-of-the-art AI and Machine Learning technologies to ensure safety and compliance in public spaces by detecting the presence and proper usage of face masks. This project aims to create a robust and efficient system that can accurately identify individuals wearing masks and alert authorities if safety protocols are not followed.

## Features

- **Real-Time Detection:** Utilizes real-time video streams to detect the presence and proper wearing of masks.
- **High Accuracy:** Employs advanced deep learning models, such as Convolutional Neural Networks (CNNs), to achieve high detection accuracy.
- **Scalability:** Designed to work efficiently across various environments, from small shops to large public spaces.
- **User-Friendly Interface:** Provides an intuitive interface for monitoring and managing alerts.
- **Performance Metrics:** Includes detailed performance metrics to track the system's effectiveness and areas for improvement.

## Technologies Used

- **Programming Languages:** Python
- **Deep Learning Frameworks:** TensorFlow, Keras
- **Computer Vision Libraries:** OpenCV
- **Deployment Tools:** Docker, Kubernetes
- **Monitoring Tools:** Grafana, Prometheus

## Installation

To set up the Mask Wear Detector locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/ASM313/mask-wear-detector.git
    cd mask-wear-detector
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python app.py
    ```

## Usage

1. **Configure Camera Feed:** Update the configuration file with your camera feed details.
2. **Run the Detector:** Start the application to begin real-time mask detection.
3. **Monitor Alerts:** Use the interface to monitor detection alerts and view detailed logs.

## Contributing

We welcome contributions from the community! If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

AWS ECR: 211125392420.dkr.ecr.ap-south-1.amazonaws.com/face_mask
