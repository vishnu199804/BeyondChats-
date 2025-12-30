import axios from "axios";
import "dotenv/config";

export async function publishArticle(title, content, source_url) {
  await axios.post(process.env.DJANGO_API, {
    title,
    content,
    source_url,
    is_updated: true
  });
}
