import AsyncStorage from '@react-native-async-storage/async-storage';

const getLabels = async () => {
    try {
        const labels = await AsyncStorage.getItem('labels');
        return labels ? JSON.parse(labels) : [];
    } catch (error) {
        console.error('Error getting labels:', error);
        return [];
    }
};

const saveLabel = async (label) => {
    try {
        const labels = await getLabels();
        labels.push(label);
        await AsyncStorage.setItem('labels', JSON.stringify(labels));
    } catch (error) {
        console.error('Error saving label:', error);
    }
}

const deleteLabel = async (label) => {
    try {
        const labels = await getLabels();
        const updatedLabels = labels.filter((l) => l !== label);
        await AsyncStorage.setItem('labels', JSON.stringify(updatedLabels));
    } catch (error) {
        console.error('Error deleting label:', error);
    }
}

export { getLabels, saveLabel, deleteLabel };
