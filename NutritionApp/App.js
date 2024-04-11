import { StyleSheet, Text, View, Button, StatusBar, SafeAreaView } from 'react-native';
import PhotoView from './views/PhotoView'; // Import the PhotoView component
import NLView from './views/NLView'; // Import the NLView component
import React, { useState} from 'react';

const App = () => {
  const [currentView, setCurrentView] = useState('PhotoView');

  const handleViewChange = (view) => {
    setCurrentView(view);
  }

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" />
      <Text style={styles.title}>Nutrition App</Text>

      <View style={{ justifyContent: 'center', alignItems: 'center' }}>
        <View style={{ flexDirection: 'row', justifyContent: 'space-around', width: '100%', marginBottom: 20 }}>
          <Button style={styles.button} title="Photo View" onPress={() => handleViewChange('PhotoView')} />
          <Button style={styles.button} title="History" onPress={() => handleViewChange('History')} />
        </View>
      </View>

      <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center'}}>
        {currentView === 'PhotoView' && <PhotoView />}
        {currentView === 'History' && <NLView />}
      </View>
    </SafeAreaView>
  );
};


const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
    marginVertical: 20,
  },
  button: {
    
  }
});

export default App;