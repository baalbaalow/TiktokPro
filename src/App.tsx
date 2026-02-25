import { motion } from "motion/react";
import { Download, Mic, RefreshCw, Volume2, Clock, CheckCircle2, Terminal, ExternalLink, Github } from "lucide-react";

export default function App() {
  const steps = [
    {
      icon: <Download className="w-6 h-6" />,
      title: "TikTok Downloader",
      description: "Seamlessly fetch videos using yt-dlp with high-quality preservation."
    },
    {
      icon: <Mic className="w-6 h-6" />,
      title: "AI Transcription",
      description: "Powered by OpenAI Whisper for near-perfect speech-to-text accuracy."
    },
    {
      icon: <RefreshCw className="w-6 h-6" />,
      title: "Copyright Rephrasing",
      description: "Intelligent NLP rewriter to ensure your content stays unique and safe."
    },
    {
      icon: <Volume2 className="w-6 h-6" />,
      title: "Edge-TTS Generation",
      description: "Premium Microsoft Azure neural voices for natural-sounding narration."
    },
    {
      icon: <Clock className="w-6 h-6" />,
      title: "Duration Sync",
      description: "Perfectly matches audio speed to video length for a professional finish."
    }
  ];

  const installCommand = "pip install yt-dlp openai-whisper moviepy pydub edge-tts gradio";

  return (
    <div className="min-h-screen bg-[#0a0a0a] text-white font-sans selection:bg-emerald-500/30">
      {/* Hero Section */}
      <header className="relative overflow-hidden pt-24 pb-16 px-6">
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full bg-[radial-gradient(circle_at_50%_0%,rgba(16,185,129,0.15),transparent_50%)]" />
        
        <div className="max-w-4xl mx-auto text-center relative z-10">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
          >
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-medium mb-6">
              <span className="relative flex h-2 w-2">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
              </span>
              v1.0.0 Release
            </div>
            <h1 className="text-6xl md:text-7xl font-bold tracking-tighter mb-6 bg-gradient-to-b from-white to-white/60 bg-clip-text text-transparent">
              TikTok Remix <span className="text-emerald-500">Pro</span>
            </h1>
            <p className="text-xl text-zinc-400 max-w-2xl mx-auto mb-10 leading-relaxed">
              The ultimate automated pipeline for content creators. Download, transcribe, rephrase, and re-voice TikTok videos with perfect duration synchronization.
            </p>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.2, duration: 0.5 }}
            className="flex flex-wrap justify-center gap-4"
          >
            <button className="px-8 py-4 bg-emerald-500 hover:bg-emerald-400 text-black font-semibold rounded-xl transition-all hover:scale-105 flex items-center gap-2 shadow-[0_0_20px_rgba(16,185,129,0.3)]">
              <Download className="w-5 h-5" />
              Get Started
            </button>
            <button className="px-8 py-4 bg-zinc-900 hover:bg-zinc-800 text-white font-semibold rounded-xl border border-white/10 transition-all flex items-center gap-2">
              <Github className="w-5 h-5" />
              View Source
            </button>
          </motion.div>
        </div>
      </header>

      {/* Features Grid */}
      <section className="py-24 px-6 bg-zinc-950/50">
        <div className="max-w-6xl mx-auto">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {steps.map((step, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1 }}
                className="p-8 rounded-2xl bg-zinc-900/50 border border-white/5 hover:border-emerald-500/30 transition-all group"
              >
                <div className="w-12 h-12 rounded-xl bg-emerald-500/10 flex items-center justify-center text-emerald-500 mb-6 group-hover:scale-110 transition-transform">
                  {step.icon}
                </div>
                <h3 className="text-xl font-bold mb-3">{step.title}</h3>
                <p className="text-zinc-400 leading-relaxed">
                  {step.description}
                </p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Installation Section */}
      <section className="py-24 px-6 relative overflow-hidden">
        <div className="max-w-4xl mx-auto">
          <div className="p-12 rounded-3xl bg-gradient-to-br from-zinc-900 to-black border border-white/10 relative z-10">
            <div className="flex items-center gap-3 mb-8">
              <Terminal className="w-8 h-8 text-emerald-500" />
              <h2 className="text-3xl font-bold tracking-tight">Installation</h2>
            </div>
            
            <div className="space-y-6">
              <p className="text-zinc-400">
                Run the following command in your terminal to install all required dependencies. Ensure you have <span className="text-white font-mono">ffmpeg</span> installed on your system.
              </p>
              
              <div className="relative group">
                <div className="absolute -inset-1 bg-gradient-to-r from-emerald-500 to-cyan-500 rounded-xl blur opacity-25 group-hover:opacity-40 transition duration-1000"></div>
                <div className="relative bg-black rounded-xl p-6 font-mono text-sm flex items-center justify-between border border-white/10 overflow-x-auto">
                  <code className="text-emerald-400 whitespace-nowrap">{installCommand}</code>
                  <button 
                    onClick={() => navigator.clipboard.writeText(installCommand)}
                    className="ml-4 p-2 hover:bg-zinc-800 rounded-lg transition-colors text-zinc-500 hover:text-white"
                    title="Copy to clipboard"
                  >
                    <Download className="w-4 h-4" />
                  </button>
                </div>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-8">
                <div className="flex items-start gap-3 p-4 rounded-xl bg-zinc-900/50 border border-white/5">
                  <CheckCircle2 className="w-5 h-5 text-emerald-500 mt-0.5 shrink-0" />
                  <div>
                    <h4 className="font-semibold mb-1 text-sm">Python 3.8+</h4>
                    <p className="text-xs text-zinc-500">Required for all libraries</p>
                  </div>
                </div>
                <div className="flex items-start gap-3 p-4 rounded-xl bg-zinc-900/50 border border-white/5">
                  <CheckCircle2 className="w-5 h-5 text-emerald-500 mt-0.5 shrink-0" />
                  <div>
                    <h4 className="font-semibold mb-1 text-sm">FFmpeg</h4>
                    <p className="text-xs text-zinc-500">Required for video processing</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-12 px-6 border-t border-white/5 text-center">
        <p className="text-zinc-500 text-sm">
          Built with ❤️ for the creator community.
        </p>
      </footer>
    </div>
  );
}
