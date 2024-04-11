import React, { useState } from "react";

import { View, Button, StyleSheet, Text } from "react-native";

const NutritionLabel = ({ label, onRemove }) => {
  // Add the useState hook to manage the showAllDetails state
  const [showAllDetails, setShowAllDetails] = useState(false);

  label = JSON.parse(label); 

  const styles = StyleSheet.create({
    container: {
      padding: 10,
      margin: 5,
      borderWidth: 1,
      borderColor: '#ddd',
      borderRadius: 5,
    },
    text: {
      fontSize: 16,
      marginBottom: 5,
    },
  });

  // Create a new Date object using the timestamp
  var date = new Date(label.date);

  return (
    <View style={styles.container}>
      {/* Display basic details and format the minutes and seconds */}
      <Text style={styles.text}>Date: {date.toDateString() + ' ' + date.toLocaleTimeString()}</Text>
      <Text style={styles.text}>Calories: {label.calories}</Text>
      <Text style={styles.text}>Total Fat: {label.total_fat} g</Text>
      <Text style={styles.text}>Total Carbs: {label.total_carbs} g</Text>
      <Text style={styles.text}>Protein: {label.protein} g</Text>
      <Text style={styles.text}>Total Sugars: {label.total_sugars} g</Text>

      {/* Button to show all details */}
      <Button
        title={showAllDetails ? 'Hide Details' : 'Show All Details'}
        onPress={() => setShowAllDetails(!showAllDetails)}
      />

      {/* Conditionally render all details based on state */}
      {showAllDetails && (
        <>
            <Text style={styles.text}>Saturated Fat: {label.saturated_fat} g</Text>
            <Text style={styles.text}>Trans Fat: {label.trans_fat} g</Text>
            <Text style={styles.text}>Cholesterol: {label.cholesterol} g</Text>
            <Text style={styles.text}>Sodium: {label.sodium} g</Text>
            <Text style={styles.text}>Dietary Fiber: {label.dietary_fiber} g</Text>
            {/* Special Nutrients Section */}
            <Text style={styles.text}>Special Nutrients:</Text>
            <Text style={styles.text}>  Calcium: {label.special_nutrients.calcium} g</Text>
            <Text style={styles.text}>  Iron: {label.special_nutrients.iron} g</Text>
            <Text style={styles.text}>  Potassium: {label.special_nutrients.potassium} g</Text>
        </>
        )}
    
        {/* Button to delete the label */}
        <Button title="Delete Label" onPress={onRemove} />
    </View>
    );
}

export default NutritionLabel;
