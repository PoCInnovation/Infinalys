export default interface Stock {
    name: string,
    trend: "up" | "down" | undefined,
    trendPercentage: number
}