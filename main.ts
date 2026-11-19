// make.fun bounty: Post a GTA 6 meme on X.
// Copies POST.json (the X post's address) to /output. That is all it does:
// the house reads the post itself from X and judges its picture and text.
// The meme (meme.png, built by build_meme.py) shows make.fun's ghost
// mascot over a Vice City sunset; the post's text carries @makefunai,
// a make.fun link, the play code and the earn-money pitch.
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";
mkdirSync(outDir, { recursive: true });
copyFileSync(join(here, "POST.json"), join(outDir, "POST.json"));
console.log("wrote " + join(outDir, "POST.json"));
