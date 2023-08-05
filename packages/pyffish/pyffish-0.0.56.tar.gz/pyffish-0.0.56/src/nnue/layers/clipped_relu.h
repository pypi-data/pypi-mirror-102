/*
  Stockfish, a UCI chess playing engine derived from Glaurung 2.1
  Copyright (C) 2004-2021 The Stockfish developers (see AUTHORS file)

  Stockfish is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  Stockfish is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

// Definition of layer ClippedReLU of NNUE evaluation function

#ifndef NNUE_LAYERS_CLIPPED_RELU_H_INCLUDED
#define NNUE_LAYERS_CLIPPED_RELU_H_INCLUDED

#include "../nnue_common.h"

namespace Eval::NNUE::Layers {

  // Clipped ReLU
  template <typename PreviousLayer>
  class ClippedReLU {
   public:
    // Input/output type
    using InputType = typename PreviousLayer::OutputType;
    using OutputType = std::uint8_t;
    static_assert(std::is_same<InputType, std::int32_t>::value, "");

    // Number of input/output dimensions
    static constexpr IndexType kInputDimensions =
        PreviousLayer::kOutputDimensions;
    static constexpr IndexType kOutputDimensions = kInputDimensions;

    // Size of forward propagation buffer used in this layer
    static constexpr std::size_t kSelfBufferSize =
        CeilToMultiple(kOutputDimensions * sizeof(OutputType), kCacheLineSize);

    // Size of the forward propagation buffer used from the input layer to this layer
    static constexpr std::size_t kBufferSize =
        PreviousLayer::kBufferSize + kSelfBufferSize;

    // Hash value embedded in the evaluation file
    static constexpr std::uint32_t GetHashValue() {
      std::uint32_t hash_value = 0x538D24C7u;
      hash_value += PreviousLayer::GetHashValue();
      return hash_value;
    }

    // Read network parameters
    bool ReadParameters(std::istream& stream) {
      return previous_layer_.ReadParameters(stream);
    }

    // Forward propagation
    const OutputType* Propagate(
        const TransformedFeatureType* transformed_features, char* buffer) const {
      const auto input = previous_layer_.Propagate(
          transformed_features, buffer + kSelfBufferSize);
      const auto output = reinterpret_cast<OutputType*>(buffer);

  #if defined(USE_AVX2)
      constexpr IndexType kNumChunks = kInputDimensions / kSimdWidth;
      const __m256i kZero = _mm256_setzero_si256();
      const __m256i kOffsets = _mm256_set_epi32(7, 3, 6, 2, 5, 1, 4, 0);
      const auto in = reinterpret_cast<const __m256i*>(input);
      const auto out = reinterpret_cast<__m256i*>(output);
      for (IndexType i = 0; i < kNumChunks; ++i) {
        const __m256i words0 = _mm256_srai_epi16(_mm256_packs_epi32(
            _mm256_load_si256(&in[i * 4 + 0]),
            _mm256_load_si256(&in[i * 4 + 1])), kWeightScaleBits);
        const __m256i words1 = _mm256_srai_epi16(_mm256_packs_epi32(
            _mm256_load_si256(&in[i * 4 + 2]),
            _mm256_load_si256(&in[i * 4 + 3])), kWeightScaleBits);
        _mm256_store_si256(&out[i], _mm256_permutevar8x32_epi32(_mm256_max_epi8(
            _mm256_packs_epi16(words0, words1), kZero), kOffsets));
      }
      constexpr IndexType kStart = kNumChunks * kSimdWidth;

  #elif defined(USE_SSE2)
      constexpr IndexType kNumChunks = kInputDimensions / kSimdWidth;

  #ifdef USE_SSE41
      const __m128i kZero = _mm_setzero_si128();
  #else
      const __m128i k0x80s = _mm_set1_epi8(-128);
  #endif

      const auto in = reinterpret_cast<const __m128i*>(input);
      const auto out = reinterpret_cast<__m128i*>(output);
      for (IndexType i = 0; i < kNumChunks; ++i) {
        const __m128i words0 = _mm_srai_epi16(_mm_packs_epi32(
            _mm_load_si128(&in[i * 4 + 0]),
            _mm_load_si128(&in[i * 4 + 1])), kWeightScaleBits);
        const __m128i words1 = _mm_srai_epi16(_mm_packs_epi32(
            _mm_load_si128(&in[i * 4 + 2]),
            _mm_load_si128(&in[i * 4 + 3])), kWeightScaleBits);
        const __m128i packedbytes = _mm_packs_epi16(words0, words1);
        _mm_store_si128(&out[i],

  #ifdef USE_SSE41
          _mm_max_epi8(packedbytes, kZero)
  #else
          _mm_subs_epi8(_mm_adds_epi8(packedbytes, k0x80s), k0x80s)
  #endif

        );
      }
      constexpr IndexType kStart = kNumChunks * kSimdWidth;

  #elif defined(USE_MMX)
      constexpr IndexType kNumChunks = kInputDimensions / kSimdWidth;
      const __m64 k0x80s = _mm_set1_pi8(-128);
      const auto in = reinterpret_cast<const __m64*>(input);
      const auto out = reinterpret_cast<__m64*>(output);
      for (IndexType i = 0; i < kNumChunks; ++i) {
        const __m64 words0 = _mm_srai_pi16(
            _mm_packs_pi32(in[i * 4 + 0], in[i * 4 + 1]),
            kWeightScaleBits);
        const __m64 words1 = _mm_srai_pi16(
            _mm_packs_pi32(in[i * 4 + 2], in[i * 4 + 3]),
            kWeightScaleBits);
        const __m64 packedbytes = _mm_packs_pi16(words0, words1);
        out[i] = _mm_subs_pi8(_mm_adds_pi8(packedbytes, k0x80s), k0x80s);
      }
      _mm_empty();
      constexpr IndexType kStart = kNumChunks * kSimdWidth;

  #elif defined(USE_NEON)
      constexpr IndexType kNumChunks = kInputDimensions / (kSimdWidth / 2);
      const int8x8_t kZero = {0};
      const auto in = reinterpret_cast<const int32x4_t*>(input);
      const auto out = reinterpret_cast<int8x8_t*>(output);
      for (IndexType i = 0; i < kNumChunks; ++i) {
        int16x8_t shifted;
        const auto pack = reinterpret_cast<int16x4_t*>(&shifted);
        pack[0] = vqshrn_n_s32(in[i * 2 + 0], kWeightScaleBits);
        pack[1] = vqshrn_n_s32(in[i * 2 + 1], kWeightScaleBits);
        out[i] = vmax_s8(vqmovn_s16(shifted), kZero);
      }
      constexpr IndexType kStart = kNumChunks * (kSimdWidth / 2);
  #else
      constexpr IndexType kStart = 0;
  #endif

      for (IndexType i = kStart; i < kInputDimensions; ++i) {
        output[i] = static_cast<OutputType>(
            std::max(0, std::min(127, input[i] >> kWeightScaleBits)));
      }
      return output;
    }

   private:
    PreviousLayer previous_layer_;
  };

}  // namespace Eval::NNUE::Layers

#endif // NNUE_LAYERS_CLIPPED_RELU_H_INCLUDED
