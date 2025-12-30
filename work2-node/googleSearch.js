import SerpApi from "google-search-results-nodejs";
import "dotenv/config";

const search = new SerpApi.GoogleSearch(process.env.SERPAPI_API_KEY);

export async function searchGoogle(query) {
  return new Promise((resolve) => {
    search.json(
      { q: query, num: 2 },
      (data) => {
        const links = data.organic_results
          .slice(0, 2)
          .map(item => item.link);
        resolve(links);
      }
    );
  });
}
