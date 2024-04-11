// PhotoView.js
import React, { useState } from 'react';
import axios from 'axios';

import { View, Button, Alert, Image, StyleSheet } from 'react-native';
import * as ImagePicker from 'expo-image-picker';

import placeholder from './../assets/images/camera.jpg';
import { saveLabel } from './../storage/importExport';

const FormData = global.FormData;
const SERVER_URL = require('./../config.json').serverURL;  // Get Server URL from JSON

const PhotoView = () => {
  const [image, setImage] = useState();

  const saveImage = async (image) => {
    try {
      // update displayed image
      setImage(image);
    } catch (error) {
      console.error('Error saving image:', error);
      Alert.alert('Error', 'Failed to save image');
    }
  };

  const takePhoto = async () => {
    // Add logic for taking a photo
    try {
      ImagePicker.requestCameraPermissionsAsync();
      await ImagePicker.requestMediaLibraryPermissionsAsync();
      const result = await ImagePicker.launchCameraAsync({
        aspect: [3, 2],
        quality: 1
      });

      if (!result.canceled) {
        await saveImage(result.assets[0].uri);
        Alert.alert('Success', 'Photo taken successfully!');
      }
    } catch (error) {
      console.error('Error taking photo:', error);
      Alert.alert('Error', 'Failed to take photo');
    }
  };

  const uploadPhoto = async () => {
    // Add logic for uploading a photo
    try {
      await ImagePicker.requestMediaLibraryPermissionsAsync();
      let result = await ImagePicker.launchImageLibraryAsync({
        mediaTypes: ImagePicker.MediaTypeOptions.Images,
        aspect: [3, 2],
        quality: 1
      });

      if (!result.canceled) {
        await saveImage(result.assets[0].uri);
        Alert.alert('Success', 'Photo uploaded successfully!');
      }
    } catch (error) {
      console.error('Error uploading photo:', error);
      Alert.alert('Error', 'Failed to upload photo');
    }
  };

  const fetchNutritionFacts = async () => {
    if (!image) {
      Alert.alert('Error', 'No image selected');
      return;
    }

    const formData = new FormData();
    formData.append("image", {
      uri: image,
      name: "image.jpg",
      type: "image/jpg"
    });

    const config = {
      headers: {
        "Content-Type": "multipart/form-data"
      }
    };

    try {
      const response = await axios.post(`${SERVER_URL}/upload`, formData, config);
      
      // check if response is valid
      if (response.status !== 200) {
        console.error('Error fetching nutrition facts:', response);
        Alert.alert('Error', 'Failed to get nutrition facts');
        return;
      }

      if (response.data.error) {
        Alert.alert('Error', response.data.error);
        return;
      }

      // Add label to storage
      let label = response.data;
      label['date'] = new Date().valueOf(); 
      await saveLabel(JSON.stringify(label));
      Alert.alert('Nutrition Facts', JSON.stringify(label, null, 2));
    } catch (error) {
      console.error('Error fetching nutrition facts:', error);
      Alert.alert('Error', 'Failed to fetch nutrition facts');
    }
  };

  return (
    <View style={{justifyContent: 'center', alignItems: 'center' }}>
      {/* Display the Image they Uploaded */}
      <Image 
        style={{ width: 250, height: 250*1.5, marginBottom: 10 }}
        source={image ? { uri: image } : placeholder}
      />
      <View style={{ flexDirection: 'row', marginBottom: 10}}>
        <Button title="Take Photo" onPress={takePhoto} />
        <Button title={"Upload Photo\n(Camera Roll)"} onPress={uploadPhoto} />
      </View>
      <Button title="Clear" onPress={() => setImage(null)} />
      <View style={{ marginBottom: 10 }} />
      <Button title="Get Nutrition Facts" onPress={fetchNutritionFacts} disabled={!image} />
    </View>
  );
};

export default PhotoView;