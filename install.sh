#!/bin/bash

echo "🔧 Installing requirements for Kunal Rajput Header Checker Tool..."
sleep 1

# Check for pip3
if ! command -v pip3 &> /dev/null
then
    echo "❌ pip3 not found. Please install Python 3 and pip3 first."
    exit
fi

# Install Python dependencies
pip3 install -r requirements.txt

echo "✅ Dependencies installed."

# Optional: make script executable
chmod +x kunal_rajput_header_checker.py

# Done
echo "🚀 You can now run the tool with:"
echo "   python3 kunal_rajput_header_checker.py"
