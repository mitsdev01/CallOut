"""
Simple tests for Callout.ai
Run with: python test_app.py
"""

import os
import sys

def test_imports():
    """Test that all required packages can be imported"""
    print("🧪 Testing imports...")
    
    required_packages = [
        ('flask', 'Flask'),
        ('werkzeug', 'Werkzeug'),
        ('requests', 'Requests'),
        ('numpy', 'NumPy'),
        ('scipy', 'SciPy'),
    ]
    
    optional_packages = [
        ('TTS', 'Coqui TTS'),
        ('torch', 'PyTorch'),
    ]
    
    failed = []
    
    # Test required packages
    for module, name in required_packages:
        try:
            __import__(module)
            print(f"✅ {name} imported successfully")
        except ImportError as e:
            print(f"❌ Failed to import {name}: {e}")
            failed.append(name)
    
    # Test optional packages
    for module, name in optional_packages:
        try:
            __import__(module)
            print(f"✅ {name} imported successfully")
        except ImportError as e:
            print(f"⚠️  {name} not available (optional): {e}")
    
    if failed:
        print(f"\n❌ Failed imports: {', '.join(failed)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("\n✅ All required packages imported successfully!\n")
    return True

def test_directories():
    """Test that required directories exist"""
    print("📁 Testing directories...")
    
    required_dirs = ['uploads', 'generated', 'templates', 'static']
    
    for dir_name in required_dirs:
        if os.path.exists(dir_name):
            print(f"✅ {dir_name}/ exists")
        else:
            print(f"⚠️  {dir_name}/ missing - creating...")
            os.makedirs(dir_name, exist_ok=True)
    
    print("\n✅ All directories ready!\n")
    return True

def test_files():
    """Test that required files exist"""
    print("📄 Testing files...")
    
    required_files = [
        'app.py',
        'requirements.txt',
        'templates/index.html',
        'static/style.css',
        'static/script.js',
    ]
    
    missing = []
    
    for file_name in required_files:
        if os.path.exists(file_name):
            print(f"✅ {file_name} exists")
        else:
            print(f"❌ {file_name} missing")
            missing.append(file_name)
    
    if missing:
        print(f"\n❌ Missing files: {', '.join(missing)}")
        return False
    
    print("\n✅ All required files present!\n")
    return True

def test_flask_app():
    """Test that Flask app can be initialized"""
    print("🌶️  Testing Flask app...")
    
    try:
        # Add current directory to path
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        
        from app import app
        
        # Test that app is a Flask instance
        from flask import Flask
        if isinstance(app, Flask):
            print("✅ Flask app initialized successfully")
            print(f"✅ App name: {app.name}")
            print(f"✅ Debug mode: {app.debug}")
        else:
            print("❌ App is not a Flask instance")
            return False
        
    except Exception as e:
        print(f"❌ Error initializing Flask app: {e}")
        return False
    
    print("\n✅ Flask app ready!\n")
    return True

def test_environment():
    """Test environment configuration"""
    print("🔧 Testing environment...")
    
    # Check for optional environment variables
    if os.getenv('USE_ELEVENLABS_API') == 'true':
        print("✅ ElevenLabs API enabled")
        if os.getenv('ELEVENLABS_API_KEY'):
            print("✅ ElevenLabs API key found")
        else:
            print("⚠️  ElevenLabs API key not set")
    else:
        print("ℹ️  Using Coqui TTS (default)")
    
    port = os.getenv('PORT', '5000')
    print(f"ℹ️  Server will run on port: {port}")
    
    print("\n✅ Environment configured!\n")
    return True

def main():
    """Run all tests"""
    print("\n" + "="*50)
    print("🎤 Callout.ai - System Tests")
    print("="*50 + "\n")
    
    tests = [
        test_directories,
        test_files,
        test_imports,
        test_flask_app,
        test_environment,
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ Test failed with error: {e}\n")
            results.append(False)
    
    # Summary
    print("="*50)
    print("📊 Test Summary")
    print("="*50)
    
    passed = sum(results)
    total = len(results)
    
    print(f"Tests passed: {passed}/{total}")
    
    if all(results):
        print("\n✅ All tests passed! Ready to run the app.")
        print("\nTo start the app:")
        print("  python app.py")
        print("\nThen open: http://localhost:5000")
    else:
        print("\n❌ Some tests failed. Please fix the issues above.")
        print("\nTry running:")
        print("  pip install -r requirements.txt")
    
    print("="*50 + "\n")
    
    return all(results)

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)


