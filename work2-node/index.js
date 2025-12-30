import axios from "axios";
import * as cheerio from "cheerio";
import dotenv from "dotenv";

dotenv.config();

/* -------------------------------
   STEP 1: Fetch articles from Django
-------------------------------- */
async function fetchArticles() {
  try {
    const res = await axios.get(process.env.DJANGO_API);
    return res.data;
  } catch (error) {
    console.error("Error fetching articles:", error.message);
    return [];
  }
}

/* -------------------------------
   STEP 2: Google search (BASIC)
   (We simulate Google search using DuckDuckGo HTML)
-------------------------------- */
async function googleSearch(query) {
  const searchUrl = `https://duckduckgo.com/html/?q=${encodeURIComponent(query)}`;

  const res = await axios.get(searchUrl, {
    headers: {
      "User-Agent": "Mozilla/5.0"
    }
  });

  const $ = cheerio.load(res.data);
  const links = [];

  $("a.result__a").each((i, el) => {
    if (i < 2) {
      links.push($(el).attr("href"));
    }
  });

  return links;
}

/* -------------------------------
   MAIN FUNCTION
-------------------------------- */
async function main() {
  console.log("Phase 2 started...\n");

  const articles = await fetchArticles();

  if (articles.length === 0) {
    console.log("No articles found");
    return;
  }

  for (const article of articles) {
    console.log("Article:", article.title);

    const links = await googleSearch(article.title);

    console.log("Found links:");
    console.log(links);
    console.log("----------------------\n");
  }
}

main();

