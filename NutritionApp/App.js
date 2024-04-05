import { StyleSheet, Text, Image, View, Button, StatusBar, SafeAreaView } from 'react-native';
import PhotoView from './views/PhotoView'; // Import the PhotoView component
import NLView from './views/NLView'; // Import the NLView component
import React, { useState} from 'react';

const App = () => {
  const [currentView, setCurrentView] = useState('PhotoView');

  const handleViewChange = (view) => {
    setCurrentView(view);
  }

  return (
    // <View style={{ flex: 1}}>
    //   {/* Your main content */}
    //   <View style={{ flex: 0.5, justifyContent:'center', alignItems: 'center' }}>
    //     <Text style={{ fontSize: 20, fontWeight: 'bold', marginBottom: 20 }}>Nutrition App</Text>
    //   </View>

    //   {/* Navigation buttons */}
    //   <View style={{ flex: 2, alignItems: 'center' }}>
    //     <Button title="Photo View" onPress={() => handleViewChange('PhotoView')} />
    //     <Button title="NL View" onPress={() => handleViewChange('NLView')} />

    //     {/* Conditional rendering */}
    //     {currentView === 'PhotoView' && <PhotoView />}
    //     {currentView === 'NLView' && <NLView />}
    //   </View>
    // </View>
    // Convert to safe area view with status bar
    <SafeAreaView style={{ flex: 1 }}>
      <StatusBar barStyle="dark-content" />
      <View style={{ justifyContent: 'top', alignItems: 'center' }}>
        <Text style={{ fontSize: 20, fontWeight: 'bold', marginBottom: 20 }}>Nutrition App</Text>
      </View>
      <View style={{ flex: 1, alignItems: 'center' }}>
        <Button title="Photo View" onPress={() => handleViewChange('PhotoView')} />
        <Button title="NL View" onPress={() => handleViewChange('NLView')} />
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