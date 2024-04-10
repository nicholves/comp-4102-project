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
    <SafeAreaView style={{ flex: 1 }}>
      <StatusBar barStyle="dark-content" />
      <View style={{ justifyContent: 'center', alignItems: 'center' }}>
        <Text style={{ fontSize: 20, fontWeight: 'bold', marginVertical: 20 }}>Nutrition App</Text>
        <View style={{ flexDirection: 'row', justifyContent: 'space-around', width: '100%', marginBottom: 20 }}>
          <Button title="Photo View" onPress={() => handleViewChange('PhotoView')} />
          <Button title="NL View" onPress={() => handleViewChange('NLView')} />
        </View>
      </View>
      <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
        {currentView === 'PhotoView' && <PhotoView />}
        {currentView === 'NLView' && <NLView />}
      </View>
    </SafeAreaView>
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