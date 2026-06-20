## ADDED Requirements

### Requirement: Audio-to-text transcription
The system SHALL use OpenAI Whisper (local model) to transcribe audio recordings of stakeholder interviews into text for requirement elicitation.

#### Scenario: Upload and transcribe audio
- **WHEN** the user uploads an audio file (WAV, MP3, M4A, or FLAC)
- **THEN** the system SHALL process the file through the local Whisper model and return a text transcription

#### Scenario: Transcription with timestamps
- **WHEN** the transcription is generated
- **THEN** the system SHALL include segment-level timestamps for traceability to the original recording

### Requirement: Multilingual transcription
The Whisper model SHALL support transcription in Spanish with the option to configure the source language.

#### Scenario: Spanish transcription
- **WHEN** the audio language is set to Spanish
- **THEN** the system SHALL pass the language parameter to Whisper for improved accuracy

### Requirement: Audio preprocessing
The system SHALL preprocess audio files to ensure compatibility with the Whisper model (resampling to 16kHz, mono channel conversion).

#### Scenario: Preprocessing pipeline
- **WHEN** an audio file is uploaded
- **THEN** the system SHALL resample to 16kHz, convert to mono, and normalize volume before transcription
