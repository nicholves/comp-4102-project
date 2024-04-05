import React, { useState, useEffect } from "react";

import { View, Button, Alert, StyleSheet, FlatList } from "react-native";

import { getLabels, deleteLabel } from "./../storage/importExport";
import NutritionLabel from "../components/NutritionLabel";

const NLView = () => {
  const [labels, setLabels] = useState([]);

  useEffect(() => {
    loadLabels();
  }, []);

  const loadLabels = async () => {
    try {
      const labels = await getLabels();
      setLabels(labels);
    } catch (error) {
      console.error("Error loading labels:", error);
      Alert.alert("Error", "Failed to load labels");
    }
  };

  const removeLabel = async (label) => {
    try {
      await deleteLabel(label);
      await loadLabels(); // Reload labels after deletion
      Alert.alert("Success", "Label removed successfully!");
    } catch (error) {
      console.error("Error removing label:", error);
      Alert.alert("Error", "Failed to remove label");
    }
  };

  return (
    <View style={styles.container}>
      <FlatList
        data={labels}
        renderItem={({ item }) => (
          <NutritionLabel label={item} onRemove={() => removeLabel(item)} />
        )}
        key = {item => item.date}
    />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    width: "80%",
  },
});

export default NLView;
