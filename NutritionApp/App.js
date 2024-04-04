import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, Image, View, Button, Alert } from 'react-native';
import PhotoView from './views/PhotoView'; // Import the PhotoView component
import axios from 'axios';

const App = () => {
  const fetchNutritionFacts = async () => {
    try {
      const response = await axios.get('https://api.nal.usda.gov/fdc/v1/foods/search?api_key=DEMO_KEY&query=apple');
      // Process response and store data as needed
      console.log(response.data);
      Alert.alert('Nutrition Facts', 'Data fetched successfully!');
    } catch (error) {
      console.error('Error fetching data:', error);
      Alert.alert('Error', 'Failed to fetch data');
    }
  };

  return (
    <View style={{ flex: 1 }}>
      {/* Your main content */}
      <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
        <Button title="Fetch Nutrition Facts" onPress={fetchNutritionFacts} />
      </View>

      {/* PhotoView component */}
      <PhotoView />
    </View>
  );
};


const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

export default App;