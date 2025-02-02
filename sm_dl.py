import yt_dlp
from rich.console import Console
from rich.prompt import Prompt
import os

console = Console()


def clear_screen():
    """ Clears the terminal screen. """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_url():
    """ Prompts the user for a video URL and a name for the downloaded file. """
    while True:
        url = Prompt.ask("\n[yellow]Enter your[/yellow] [bold green]URL[/bold green] [yellow]here[/yellow]").strip()
        if url.lower() in ["quit", "exit"]:
            return None, None  # Signal to exit the loop

        name = Prompt.ask("\n[yellow]Enter your[/yellow] [bold green]NAME[/bold green] [yellow]for the video[/yellow]").strip()
        if name.lower() in ["quit", "exit"]:
            return None, None  # Signal to exit the loop

        if url and name:
            return url, name  # Return valid inputs
        else:
            console.print("[red]Invalid input! Please enter both URL and name.[/red]")


def download_video(url, name):
    """ Downloads the video using yt-dlp with dynamic output filename. """
    output_path = f"videos/{name}.mp4"  # Store in 'videos' folder with chosen name

    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path,  # Apply dynamic filename
        'noplaylist': True,
        'quiet': False,  # Show yt-dlp output
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        console.print(f"\n[bold green]Downloading:[/bold green] {name} ...")
        ydl.download([url])

    console.print("[bold cyan]Download complete![/bold cyan] ✅")


def main():
    """ Main function to loop until user quits. """
    clear_screen()
    console.print(
        "[bold yellow]Welcome to my [/bold yellow][bold green]Social Media Video[/bold green] [bold red]Downloader[/bold red]\n")
    console.print("type '[bold]quit[/bold]' at any time to exit\n")

    while True:
        url, name = get_url()
        if not url or not name:
            console.print("[bold red]Exiting program. Goodbye![/bold red] 👋")
            break  # Exit the loop if user types "quit" or "exit"

        download_video(url, name)


if __name__ == "__main__":
    main()
