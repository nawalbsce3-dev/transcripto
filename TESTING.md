# 🧪 Testing Guide - Transcripto

## Testing the Backend API

### 1. Health Check Test

**Using curl:**
```bash
curl http://localhost:5000/api/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "service": "Transcripto Backend",
  "model": "base",
  "version": "1.0.0"
}
```

**Using browser:**
Visit: `http://localhost:5000/api/health`

---

### 2. Transcription Test (with curl)

**Prepare a test audio file:**
Save any short audio clip as `test.mp3`

**Test transcription:**
```bash
curl -X POST http://localhost:5000/api/transcribe \
  -F "audio=@test.mp3"
```

**Expected Response:**
```json
{
  "success": true,
  "transcription": "Your transcribed text will appear here...",
  "language": "en",
  "filename": "test.mp3"
}
```

---

### 3. Error Testing

**Test missing file:**
```bash
curl -X POST http://localhost:5000/api/transcribe
```

**Expected:** `400 Bad Request` with error message

**Test invalid file type:**
```bash
curl -X POST http://localhost:5000/api/transcribe \
  -F "audio=@document.pdf"
```

**Expected:** `400 Bad Request` - "File type not supported"

---

## Testing the Frontend

### 1. Basic Functionality Test

1. **Start both servers:**
   - Backend: `cd backend && python app.py`
   - Frontend: `npm run dev`

2. **Open browser:**
   - Navigate to `http://localhost:5173`

3. **Visual checks:**
   - ✅ Topbar with "Transcripto" title visible
   - ✅ Hero section with gradient background
   - ✅ Upload dropzone visible
   - ✅ Convert button present
   - ✅ Output section ready
   - ✅ Feature cards displayed

### 2. Upload Test

**Test 1: Click Upload**
1. Click the upload dropzone
2. Select an audio file (MP3, WAV, M4A)
3. ✅ File name should appear
4. ✅ File size should display
5. ✅ Status should show "Idle"

**Test 2: Drag & Drop**
1. Drag an audio file over the dropzone
2. ✅ Dropzone should highlight
3. Drop the file
4. ✅ File info should appear

**Test 3: Invalid File**
1. Try uploading a non-audio file (PDF, DOCX)
2. ✅ Should show error message
3. ✅ Should not accept file

### 3. Conversion Test

**Test Real Transcription:**
1. Upload a short audio file (30-60 seconds)
2. Click "Convert to Text"
3. ✅ Button should show loading spinner
4. ✅ Status should change to "Processing"
5. ✅ Wait 10-30 seconds (depending on file length)
6. ✅ Status should change to "Completed"
7. ✅ Transcription text should appear in output panel

**Test Error Handling:**
1. Stop the backend server
2. Try to convert a file
3. ✅ Should show error: "Failed to transcribe audio"
4. ✅ Status should return to "Idle"

### 4. Output Actions Test

**Test Copy:**
1. After successful transcription
2. Click "Copy Text" button
3. ✅ Button text should change to "Copied!"
4. ✅ Paste text elsewhere to verify

**Test Download:**
1. After successful transcription
2. Click "Download .txt" button
3. ✅ File `transcription.txt` should download
4. ✅ Open file to verify content

### 5. Responsive Design Test

**Desktop (1920x1080):**
- ✅ Hero grid layout (2 columns)
- ✅ Workspace sections visible
- ✅ Feature grid (4 columns)

**Tablet (768px):**
- ✅ Hero stacks to 1 column
- ✅ Upload/output stack vertically
- ✅ Feature grid adjusts

**Mobile (375px):**
- ✅ All content readable
- ✅ Touch targets large enough
- ✅ Dropzone usable
- ✅ Buttons accessible

---

## Integration Testing

### Full Flow Test

**Scenario:** User transcribes a meeting recording

1. **Setup:**
   - Backend running on :5000
   - Frontend running on :5173
   - Have test audio file ready

2. **Steps:**
   ```
   1. Open http://localhost:5173
   2. Drag audio file to dropzone
   3. Verify file info displays
   4. Click "Convert to Text"
   5. Observe "Processing" status
   6. Wait for completion
   7. Read transcription
   8. Click "Copy Text"
   9. Paste in notepad - verify
   10. Click "Download .txt"
   11. Open downloaded file - verify
   12. Click "Reset" button
   13. Verify clean slate
   ```

3. **Expected Results:**
   - ✅ All steps complete without errors
   - ✅ Transcription is accurate
   - ✅ Copy/download work correctly
   - ✅ UI remains responsive throughout

---

## Performance Testing

### Backend Performance

**Test 1: Small File (30 sec audio)**
```bash
time curl -X POST http://localhost:5000/api/transcribe \
  -F "audio=@small.mp3"
```
**Expected:** ~5-15 seconds (base model)

**Test 2: Medium File (2 min audio)**
```bash
time curl -X POST http://localhost:5000/api/transcribe \
  -F "audio=@medium.mp3"
```
**Expected:** ~20-40 seconds (base model)

**Test 3: Large File (5 min audio)**
```bash
time curl -X POST http://localhost:5000/api/transcribe \
  -F "audio=@large.mp3"
```
**Expected:** ~60-120 seconds (base model)

### Frontend Performance

**Test Loading Speed:**
1. Open DevTools → Network
2. Reload page
3. ✅ Initial load < 2 seconds
4. ✅ All assets load successfully

**Test Responsiveness:**
1. Open DevTools → Performance
2. Start recording
3. Upload file and convert
4. Stop recording
5. ✅ No long tasks (> 50ms)
6. ✅ Smooth animations

---

## Browser Compatibility Testing

Test on:
- ✅ Chrome (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Edge (latest)

**Check:**
- File upload works
- Drag & drop works
- Fetch API calls work
- Clipboard API works
- Download works
- UI renders correctly

---

## Security Testing

### 1. File Type Validation

**Test malicious extensions:**
```bash
# Try .exe file
curl -X POST http://localhost:5000/api/transcribe \
  -F "audio=@malicious.exe"
# Expected: 400 Bad Request
```

### 2. File Size Limits

**Test oversized file:**
```bash
# Create 30MB file
dd if=/dev/zero of=large.mp3 bs=1M count=30

curl -X POST http://localhost:5000/api/transcribe \
  -F "audio=@large.mp3"
# Expected: 413 Request Entity Too Large
```

### 3. CORS Testing

**Test from unauthorized origin:**
```javascript
// From browser console on different domain
fetch('http://localhost:5000/api/transcribe', {
  method: 'POST',
  body: formData
})
// Expected: CORS error (blocked)
```

---

## Common Test Cases

### ✅ Success Cases

1. Upload MP3, convert → success
2. Upload WAV, convert → success
3. Upload M4A, convert → success
4. Copy transcription → success
5. Download transcription → success
6. Reset and repeat → success

### ❌ Error Cases

1. Upload without file → error message
2. Upload PDF → rejected
3. Backend offline → error message
4. Network error → error message
5. Large file (>25MB) → rejected

---

## Debugging Tips

### Backend Not Starting?

```bash
# Check Python version
python --version  # Should be 3.8+

# Check FFmpeg
ffmpeg -version

# Check virtual environment
which python  # Should point to venv

# View detailed errors
python app.py  # Read console output
```

### Frontend Not Connecting?

```javascript
// Check in browser console
console.log(import.meta.env.VITE_API_URL)
// Should output: http://localhost:5000

// Test API manually
fetch('http://localhost:5000/api/health')
  .then(r => r.json())
  .then(console.log)
```

### Transcription Not Working?

1. Check backend logs for errors
2. Verify Whisper model loaded
3. Check audio file format
4. Try smaller audio file first
5. Test with curl command

---

## Automated Testing (Future)

### Backend Tests (pytest)

```python
# test_api.py
def test_health_check():
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_transcribe_valid_audio():
    with open('test.mp3', 'rb') as audio:
        response = client.post('/api/transcribe', 
            data={'audio': audio})
    assert response.status_code == 200
    assert 'transcription' in response.json
```

### Frontend Tests (Vitest)

```javascript
// App.test.js
test('uploads file and displays name', async () => {
  const file = new File(['audio'], 'test.mp3', { type: 'audio/mp3' })
  // ... test file upload
  expect(screen.getByText('test.mp3')).toBeInTheDocument()
})
```

---

## Test Checklist

Before considering done:

**Backend:**
- [ ] Health check responds
- [ ] Transcription endpoint works
- [ ] Error handling works
- [ ] File cleanup happens
- [ ] Logs are clear

**Frontend:**
- [ ] Upload works (click + drag)
- [ ] Validation works
- [ ] API calls succeed
- [ ] Transcription displays
- [ ] Copy/download work
- [ ] Reset works
- [ ] Responsive on all sizes

**Integration:**
- [ ] Full flow works end-to-end
- [ ] Error messages are helpful
- [ ] Performance is acceptable
- [ ] UI remains responsive

---

**Happy Testing! 🧪✅**
