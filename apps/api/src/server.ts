import express, { Request, Response } from 'express';
import cors from 'cors';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 5000;

// Essential middleware
app.use(cors());
app.use(express.json());

// Basic health check endpoint
app.get('/api/health', (req: Request, res: Response) => {
  res.status(200).json({
    status: 'ok',
    service: 'FieldShift AI Backend (apps/api)',
    timestamp: new Date().toISOString()
  });
});

// Root welcome route
app.get('/', (req: Request, res: Response) => {
  res.status(200).json({
    message: 'Welcome to FieldShift AI API'
  });
});

app.listen(PORT, () => {
  console.log(`[FieldShift AI] API Server running on http://localhost:${PORT}`);
});

