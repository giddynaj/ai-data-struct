# dataset_preprocessor.py - A mini AI data organizer

class ImageDataset:
    def __init__(self):
        # Lists that grow as we add data (like training an AI)
        self.images = []
        self.labels = []
        self.metadata = []

    def add_sample(self, image_path, label, dimensions):
        """Add a new training sample - like feeding data to an AI"""
        # Each image is a tuple of (path, size_bytes)
        image_info = (image_path, self.calculate_size(image_path))

        self.images.append(image_info)
        self.labels.append(label)
        # Metadata as tuple: (width, height, channels)
        self.metadata.append(dimensions)

    def calculate_size(self, path):
        """Simulate calculating file size"""
        return len(path) * 1024 # Simplified calculation

    def get_stats(self):
        """Analyze the dataset - like AI model evaluation"""
        total_samples = len(self.images)
        unique_labels = list(set(self.labels))

        # Calculate label distribution
        label_counts = {}
        for label in self.labels:
            label_counts[label] = label_counts.get(label, 0) + 1

        return {
            'total_samples': total_samples,
            'unique_labels': unique_labels,
            'label_distribution': label_counts,
            'average_size': sum(img[1] for img in self.images) / total_samples
        }

    def filter_by_label(self, target_label):
        """Filter data like AI systems do during training"""
        filtered_indicies = [ i for i, label in enumerate(self.labels)
                             if label == target_label]
        filtered_images = [self.images[i] for i in filtered_indicies]
        filtered_metadata = [self.metadata[i] for i in filtered_indicies]

        return filtered_images, filtered_metadata

# Demo Using our AI style data processor
def main():
    dataset = ImageDataset()

    # Add trainoing samples like feeding data to an AI model
    dataset.add_sample('cat_001.jpg', "cat", (224, 224, 3))
    dataset.add_sample('dog_001.jpg', "dog", (224, 224, 3))
    dataset.add_sample('cat_002.jpg', "cat", (256, 256, 3))
    dataset.add_sample('bird_001.jpg', "bird", (224, 224, 3))

    stats = dataset.get_stats()
    print("Dataset Analysis")
    print(f"Total samples: { stats['total_samples']}")
    print(f"Categories: {stats['unique_labels']}")
    print(f"Label distribution: {stats['label_distribution']}")

    #Filter data (common AI operation)
    cat_images, cat_metadata = dataset.filter_by_label("cat")
    print(f"\nFound {len(cat_images)} cat images")

    #Show how lists and tuples work together
    for i, (image_info, metadata) in enumerate(zip(cat_images, cat_metadata)):
        path, size = image_info #unpack tuple
        width, height, channels = metadata #unpack tuple
        print(f"Cat {i+1}: {path} ({width}x{height}, {size} bytes)")

if __name__ == "__main__":
    main()
