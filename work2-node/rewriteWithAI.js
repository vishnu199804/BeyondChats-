import OpenAI from "openai";
import "dotenv/config";

const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

export async function rewriteArticle(original, references, links) {
  const prompt = `
Rewrite this article using reference content.
Original:
${original}

References:
${references.join("\n")}

Add citations at bottom:
${links.join("\n")}
`;

  const response = await client.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [{ role: "user", content: prompt }],
  });

  return response.choices[0].message.content;
}
